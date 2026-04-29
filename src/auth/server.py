# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""
import grpc 

from concurrent import futures
import logging

from protos import auth_pb2
from protos import auth_pb2_grpc
from core.database import SessionLocal
from core.validators import is_valid_email, is_strong_password
from core.hashing import criptography, verify_password
from models.user import User
from core.security import create_token, decode_token
from datetime import timedelta
from sqlalchemy.exc import IntegrityError



class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def RegisterUser(self, request, context):
        
        if not is_valid_email(request.email):
            return auth_pb2.RegisterResponse(
                success=False,
                message='E-mail inválido',
                user_id=''
            )
            
        is_strong, error_msg = is_strong_password(request.password)
        if not is_strong:
            return auth_pb2.RegisterResponse(
                success=False,
                message=error_msg,
                user_id=''
            )
            
        with SessionLocal() as db:
            try:
                print('entrou')
                user_exists = db.query(User).filter(User.email == request.email).first()
                
                if user_exists:
                    return auth_pb2.RegisterResponse(
                        success=False,
                        message="Já existe usuário com esse e-mail",
                        user_id=''
                    )
                
                hashed_pass = criptography(request.password)
                
                new_user = User(email=request.email, hashed_password=hashed_pass,name=request.name)
            
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
            
                return auth_pb2.RegisterResponse(
                    success=True,
                    message="Usuário cadastrado com sucesso",
                    user_id=new_user.user_id
                )
            except IntegrityError:
                db.rollback() 
                return auth_pb2.RegisterResponse(success=False, message="Conflito: E-mail já está em uso.", user_id="")
            except Exception as e:
                print(e)
                db.rollback() 
                                
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details("Erro interno ao processar a requisição no banco.")
                
                return auth_pb2.RegisterResponse(success=False, message="Erro interno no servidor.", user_id="")
        
    def Login(self,request,context):
        
        with SessionLocal() as db:
            try:
                user = db.query(User).filter(User.email == request.email).first()

                if not user or not verify_password(request.password, user.hashed_password):
                    return auth_pb2.LoginResponse(
                        success=False,
                        token='',
                        message='Erro no servidor'
                    )
                    
                access_token = create_token(user.user_id)
                
                # verificar se vai precisar do refresh_token
                # refresh_token = create_token(user.user_id, duration_token=timedelta(days=7))
                
                return auth_pb2.LoginResponse(
                    success=True,
                    token=access_token,
                    message='Login realizado com sucesso!'
                )
            except Exception as e:
                print(f"Erro no banco: {e}")
                return auth_pb2.LoginResponse(
                    success=False,
                    token='',
                    message='Erro no servidor'
                )
    
    def ValidateToken(self,request,context):
        payload = decode_token(request.token)
        
        if type(payload) is dict and "error" in payload:
            return auth_pb2.ValidateTokenResponse(
                is_valid=False,
                user_id='',
                email=''
            )
            
        return auth_pb2.ValidateTokenResponse(
            is_valid=True,
            user_id=payload, # O nosso decode atual retorna diretamente o user_id (string)
            email=''
        )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

