from assertpy import assert_that
from src.conditions import status_code, body
from src.services import UserApiService


def test_user_can_change_password():
    user = {"email": "xogimuvi@smart-mail.info", "password": "123qwe", "confirmPassword": "123qwe"}
    response = UserApiService().change_password(user)
    response.should_have(status_code(200))


def test_not_existed_user_cannot_change_password(faker):
    user = {"email": faker.email(), "password": "123qwe", "confirmPassword": "123qwe"}
    response = UserApiService().change_password(user)
    response.should_have(status_code(400))
    response.should_have(body('Message', assert_that({'Message': 'Користувача з таким логіном не знайдено'}).contains_value('Користувача з таким логіном не знайдено')))