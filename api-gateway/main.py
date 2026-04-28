import grpc
import auth_pb2
import auth_pb2_grpc
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginSchema(BaseModel):
    email: str
    password: str

@app.post("/api/login")
async def login(data: LoginSchema):
    try:
        
        channel = grpc.insecure_channel('localhost:50051')
        stub = auth_pb2_grpc.AuthServiceStub(channel)

        
        response = stub.Login(auth_pb2.LoginRequest(
            email=data.email,
            password=data.password
        ))

        
        return {"token": response.token}

    except grpc.RpcError as e:
  
        raise HTTPException(status_code=401, detail="Erro na autenticação ou serviço fora do ar")
    

class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str


@app.post("/api/signup")
async def signup(data: RegisterSchema):
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = auth_pb2_grpc.AuthServiceStub(channel)

        
        response = stub.RegisterUser(auth_pb2.RegisterRequest(
            name=data.name,
            email=data.email,
            password=data.password
        ))

        return {"success": response.success, "message": response.message}
    except grpc.RpcError:
        raise HTTPException(status_code=500, detail="Erro ao falar com serviço de Auth")

@app.get("/")
def read_root():
    return {"message": "API Gateway Online"}