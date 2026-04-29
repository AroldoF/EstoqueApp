# produtos/auth.py
import grpc
from .protos import auth_pb2, auth_pb2_grpc
from ninja.security import HttpBearer

class GrpcAuth(HttpBearer):
    def authenticate(self, request, token):
        # Conecta ao serviço de Auth que você já tem
        channel = grpc.insecure_channel('localhost:50051')
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        
        try:
            # Chama o ValidateToken do seu .proto
            response = stub.ValidateToken(auth_pb2.ValidateTokenRequest(token=token))
            
            if response.is_valid:
                # Retornamos um dicionário com os dados do usuário. 
                # O Django Ninja vai colocar isso dentro de 'request.auth'
                return {
                    "user_id": response.user_id,
                    "email": response.email
                }
        except grpc.RpcError:
            return None # Retorna 401 Unauthorized automaticamente
        return None

grpc_auth = GrpcAuth()