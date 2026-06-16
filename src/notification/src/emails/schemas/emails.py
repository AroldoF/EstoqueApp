from pydantic import BaseModel

class EmailPayload(BaseModel):
    to_first_name: str
    to_email: str
    subject: str
    confirmation_url: str
    template_name: str
    context: dict