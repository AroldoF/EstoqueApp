# from contextlib import asynccontextmanager
# from faststream import FastStream
# from src.history.database import init_db, close_db
# from infra.messaging.broker import broker


# # 2. Gerenciador do Ciclo de Vida
# @asynccontextmanager
# async def lifespan(app: FastStream):
#     # 👇 [PASSO 1] Roda antes de tudo. Ideal para o Banco de Dados.
#     await init_db()
    
#     # 🚀 [PASSO 2] O FastStream assume o comando aqui:
#     # Ele liga o broker automaticamente e começa a processar as mensagens.
#     yield  
    
#     # 🛑 [PASSO 3] Você apertou Ctrl+C:
#     # O FastStream desliga o broker e para as filas ANTES de descer para a próxima linha.
    
#     # 👇 [PASSO 4] Roda por último, limpando os recursos com segurança.
#     await close_db()

# # 3. Une o App ao broker e ao ciclo de vida
# app = FastStream(broker, lifespan=lifespan)

# # 4. Carrega os handlers (mantenha no final para evitar importação circular)
# from infra.messaging.handlers.save_notification import save_notifications_handler
# from infra.messaging.handlers.send_email import handler_send_email