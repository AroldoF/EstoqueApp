import os
from tortoise import Tortoise

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://db.sqlite3")

TORTOISE_CONFIG = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["src.history.models"],  # Caminho para sua model
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC"
}

async def init_db():
    """Inicializa as conexões com o banco de dados."""
    await Tortoise.init(config=TORTOISE_CONFIG)
    
    # Cria as tabelas automaticamente se elas não existirem
    await Tortoise.generate_schemas()

    print("🔋 Conexão com o Banco de Dados (Tortoise ORM) estabelecida.")

async def close_db():
    """Fecha as conexões de forma segura."""
    await Tortoise.close_connections()
    print("🔌 Conexão com o Banco de Dados encerrada.")