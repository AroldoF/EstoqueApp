import logging
from email.message import EmailMessage
import aiosmtplib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Dict, Any
from ..schemas.emails import EmailPayload


# Configuração básica de log (deve ser feita no ponto de entrada da aplicação)
logger = logging.getLogger(__name__)

class EmailSender:
    def __init__(self, smtp_config: Any, templates_dir: str = "templates"):
        """
        Inicializa o enviador de e-mails recebendo as configurações por injeção de dependência.
        """
        self.host = smtp_config.host
        self.port = smtp_config.port or 587
        self.username = smtp_config.username
        self.password = smtp_config.password.get_secret_value()

        self.use_tls = smtp_config.scheme == "smtps"
        self.start_tls = not self.use_tls and self.port == 587

        self.jinja_env = Environment(
            loader=FileSystemLoader(templates_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    async def build_message(self, to_email: str, subject: str, template_name: str, context: Dict[str, Any]) -> EmailMessage:
        """
        Gera a mensagem com contexto dinâmico para o template.
        """
        template = self.jinja_env.get_template(template_name)
        html_content = template.render(context)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_email
        
        msg.set_content("Seu cliente de e-mail não suporta visualização em HTML.")
        msg.add_alternative(html_content, subtype='html')

        return msg

    async def send(self, notification: EmailPayload) -> bool:
        """
        Envia um único e-mail. Retorna True se enviado com sucesso, ou levanta uma exceção.
        """
        msg = await self.build_message(notification.to_email, notification.subject, notification.template_name, notification.context)

        try:
            # Para envio único, o gerenciador de contexto garante o fechamento correto da conexão
            async with aiosmtplib.SMTP(
                hostname=self.host,
                port=self.port,
                use_tls=self.use_tls,
                start_tls=self.start_tls
            ) as client:
                await client.login(self.username, self.password)
                await client.send_message(msg)
                
            logger.info(f"E-mail enviado com sucesso para {notification.to_email}")
            return True
            
        except aiosmtplib.SMTPException as e:
            logger.error(f"Erro SMTP ao enviar e-mail para {notification.to_email}: {e}", exc_info=True)
            raise  # Repassa o erro para a camada superior tratar (ex: dar retry na fila)
        except Exception as e:
            logger.critical(f"Erro inesperado no disparo de e-mail: {e}", exc_info=True)
            raise