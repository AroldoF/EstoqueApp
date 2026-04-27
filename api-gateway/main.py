import grpc
import auth_pb2
import auth_pb2_grpc
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Liberar o React para conversar com o Gateway
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # URL do seu Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para receber os dados do formulário React
class LoginSchema(BaseModel):
    email: str
    password: str

@app.post("/api/login")
async def login(data: LoginSchema):
    try:
        # 1. Cria o canal de comunicação com o servidor gRPC da Renata
        # Assumindo que o dela roda na porta 50051
        channel = grpc.insecure_channel('localhost:50051')
        stub = auth_pb2_grpc.AuthServiceStub(channel)

        # 2. Envia os dados para o microserviço de Auth
        response = stub.Login(auth_pb2.LoginRequest(
            email=data.email,
            password=data.password
        ))

        # 3. Se deu certo, devolve o token para o React
        return {"token": response.token}

    except grpc.RpcError as e:
        # Se o servidor da Renata estiver offline ou as credenciais erradas
        raise HTTPException(status_code=401, detail="Erro na autenticação ou serviço fora do ar")

@app.get("/")
def read_root():
    return {"message": "API Gateway Online"}