from pydantic import BaseModel, constr, Field


class UserRegistration(BaseModel):
    first_name: str = Field(max_length=30)
    second_name: str = Field(max_length=30)
    email: str = Field(max_length=30)
    password: str = Field(min_length=6, max_length=20)
    telegram_account: str = Field(default=None)


