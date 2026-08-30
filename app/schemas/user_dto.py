from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr, StringConstraints

UserName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=100),
]


class UserCreateDTO(BaseModel):
    name: UserName
    email: EmailStr
    password: str


class UserUpdateDTO(BaseModel):
    name: UserName | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
