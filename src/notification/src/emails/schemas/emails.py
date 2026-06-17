from pydantic import BaseModel

class EmailPayload(BaseModel):
    to_email: str
    subject: str
    template_name: str
    name_product: str
    total_items: int
    context: dict