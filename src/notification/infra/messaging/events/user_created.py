from dataclasses import dataclass

@dataclass
class UserCreatedEvent:
    user_id: int
    first_name: str
    email: str
    confirmation_key: str
    confirmation_url: str
    template_prefix: str
