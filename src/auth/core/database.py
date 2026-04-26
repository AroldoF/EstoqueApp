from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

from core.config import settings

# Quando mudar para PostgreSQL, o connect_args pode ser removido.
engine = create_async_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session: 
        yield session