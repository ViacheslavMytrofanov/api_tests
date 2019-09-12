from src.conditions import status_code, body
from src.services import UserApiService
from assertpy import assert_that


def test_user_can_signup_with_valid_credentials(faker):
    user = {"firstName": faker.name(), "lastName": faker.name(), "email": faker.email(),
            "password": "123456", "confirmPassword": "123456", "emailConfirmed": True}

    response = UserApiService().create_user(user)
    response.should_have(status_code(201))
    response.should_have(body("succeeded", assert_that({'succeeded': 'true'}).contains_value('true')))


def test_user_cannot_signup_with_same_credentials(faker):
    user = {"firstName": faker.name(), "lastName": faker.name(), "email": "xogimuvi@smart-mail.info",
            "password": "123456", "confirmPassword": "123456", "emailConfirmed": True}

    response = UserApiService().create_user(user)
    response.should_have(status_code(500))
    response.should_have(body("Message", assert_that({'Message': 'AdSaver. User allready exists'})
                              .contains_value('AdSaver. User allready exists ')))
