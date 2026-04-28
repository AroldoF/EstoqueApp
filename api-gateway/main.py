import grpc
import auth_pb2
import auth_pb2_grpc
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

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



PRODUCT_SERVICE_URL = "http://localhost:8001/api"

@app.get("/api/product")
async def list_products():
    async with httpx.AsyncClient() as client:
        try:
            
            response = await client.get(f"{PRODUCT_SERVICE_URL}/product")
            return response.json()
        except Exception:
            raise HTTPException(status_code=503, detail="Erro ao buscar produtos no estoque")
        

@app.post("/api/product") 
async def create_product(product_data: dict):
    async with httpx.AsyncClient() as client:
        try:
           
            response = await client.post(f"{PRODUCT_SERVICE_URL}/product", json=product_data)
            return response.json()
        except Exception:
            raise HTTPException(status_code=503, detail="Erro ao salvar no estoque")


@app.get("/api/product/{product_id}")
async def get_product(product_id: int):
    async with httpx.AsyncClient() as client:
        try:
            
            response = await client.get(f"{PRODUCT_SERVICE_URL}/product/{product_id}/")
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Produto não encontrado no banco")
            return response.json()
        except Exception:
            raise HTTPException(status_code=503, detail="Erro ao buscar produto")


@app.patch("/api/product/{product_id}")
async def update_product(product_id: int, product_data: dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(
                f"{PRODUCT_SERVICE_URL}/product/{product_id}/", 
                json=product_data
            )
            return response.json()
        except Exception:
            raise HTTPException(status_code=503, detail="Erro ao atualizar produto")


@app.delete("/api/product/{product_id}")
async def delete_product(product_id: int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(f"{PRODUCT_SERVICE_URL}/product/{product_id}/")
            return {"message": "Produto deletado com sucesso"}
        except Exception:
            raise HTTPException(status_code=503, detail="Erro ao deletar produto")
        
@app.get("/")
def read_root():
    return {"message": "API Gateway Online"}