from pydantic import BaseModel


class RegistrationValidator(BaseModel):
    name: str
    phone_number: int
    city: str
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
