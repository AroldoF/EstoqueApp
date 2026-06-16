from functools import cached_property

from pydantic import AnyUrl, BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import unquote

class SMTPConfig(BaseModel):
    scheme: str
    host: str
    port: int
    username: str
    password: SecretStr


class Settings(BaseSettings):
    messaging_url: str
    smtp_url: AnyUrl

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @cached_property
    def smtp(self) -> SMTPConfig:
        return SMTPConfig(
            scheme=self.smtp_url.scheme,
            host=self.smtp_url.host,
            port=self.smtp_url.port or 587,
            username=unquote(self.smtp_url.username or ""),
            password=SecretStr(self.smtp_url.password or ""),
        )


settings = Settings()