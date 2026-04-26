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


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def RegisterUser(self, request, context):
        return auth_pb2.RegisterResponse(
            success=True,
            message="Usuário cadastrado com sucesso",
            user_id='fake-123'
        )
        
    def Login(self,request,context):
        return auth_pb2.LoginResponse(
            sucess=True,
            token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
            message='Login realizado com sucesso!'
        )
    
    def ValidateToken(self,request,context):
        return auth_pb2.ValidateTokenResponse(
            is_valid=True,
            user_id='fake-123',
            email='user@testeapp.com'
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

