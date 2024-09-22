import allure
import pytest
from selenium import webdriver

from pages.registration_page import Registration_page, User


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.description("Test registration")
def test_registration(driver):
    print('Start Registration Test')

    try:
        # Регистрация пользователя
        registration_page = Registration_page(driver)
        user = registration_page.create_user()
        registration_page.register_user(user)

        # Добавьте проверки после регистрации, если необходимо

    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

    finally:
        print('Finish Registration Test')