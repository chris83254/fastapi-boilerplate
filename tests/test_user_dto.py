import pytest
from pydantic import ValidationError

from app.schemas.user_dto import UserCreateDTO, UserUpdateDTO


def test_register_rejects_blank_name(client):
    response = client.post(
        "/auth/register",
        json={
            "name": "   ",
            "email": "blank@example.com",
            "password": "testpassword123",
        },
    )

    assert response.status_code == 422


@pytest.mark.parametrize("name", ["", "   ", "\t\n"])
def test_user_dtos_reject_blank_names(name):
    with pytest.raises(ValidationError):
        UserCreateDTO(
            name=name,
            email="blank@example.com",
            password="testpassword123",
        )

    with pytest.raises(ValidationError):
        UserUpdateDTO(name=name)


def test_user_dtos_trim_names():
    created = UserCreateDTO(
        name="  Test User  ",
        email="test@example.com",
        password="testpassword123",
    )
    updated = UserUpdateDTO(name="  Renamed User  ")

    assert created.name == "Test User"
    assert updated.name == "Renamed User"
