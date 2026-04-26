import grpc
from protos import auth_pb2
from protos import auth_pb2_grpc

def run_tests():
    # 1. Abre o canal de comunicação com o servidor gRPC
    print("Tentando conectar ao servidor gRPC na porta 50051...")
    with grpc.insecure_channel('localhost:50051') as channel:
        # O Stub é o "cliente" que sabe quais funções existem no servidor
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        
        email_teste = "renata2025@estoqueapp.com"
        senha_teste = "SenhaForte123"

        print("\n--- TESTE 1: CADASTRO ---")
        try:
            register_req = auth_pb2.RegisterRequest(
                email=email_teste,
                password=senha_teste,
                name="Usuária Teste"
            )
            register_res = stub.RegisterUser(register_req)
            print(f"Sucesso: {register_res.success}")
            print(f"Mensagem: {register_res.message}")
            print(f"User ID: {register_res.user_id}")
        except grpc.RpcError as e:
            print(f"Falha na chamada gRPC: {e.details()}")

        print("\n--- TESTE 2: LOGIN ---")
        token_gerado = ""
        try:
            login_req = auth_pb2.LoginRequest(
                email=email_teste,
                password=senha_teste
            )
            login_res = stub.Login(login_req)
            print(f"Sucesso: {login_res.success}")
            print(f"Mensagem: {login_res.message}")
            if login_res.success:
                token_gerado = login_res.token
                print(f"Token JWT recebido: {token_gerado[:30]}... (truncado)")
        except grpc.RpcError as e:
            print(f"Falha na chamada gRPC: {e.details()}")

        print("\n--- TESTE 3: VALIDAÇÃO DO TOKEN ---")
        if token_gerado:
            try:
                validate_req = auth_pb2.ValidateTokenRequest(token=token_gerado)
                validate_res = stub.ValidateToken(validate_req)
                print(f"Token é válido?: {validate_res.is_valid}")
                print(f"User ID recuperado: {validate_res.user_id}")
            except grpc.RpcError as e:
                print(f"Falha na chamada gRPC: {e.details()}")
        else:
            print("Pulo do teste de validação (nenhum token foi gerado no login).")

if __name__ == '__main__':
    run_tests()