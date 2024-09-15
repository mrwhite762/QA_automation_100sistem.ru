import pytest
from selenium import webdriver

from pages.login_pag import Login_account

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_with_email(driver):
    print('НАЧАЛО ПРОВЕРКИ ВХОДА С EMAIL (С ВЫХОДОМ ИЗ АККАУНТА)')

    try:
        # Вход по email
        login_page = Login_account(driver)
        email = "kudrjavtsevzinovi@example.org"
        password = "*+1M^Fkl"
        login_page.login_with_email(email, password)
        login_page.logout()

        # Добавьте проверки после входа, если необходимо

    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

    finally:
        print('ОКОНЧАНИЕ ПРОВЕРКИ ВХОДА С EMAIL (С ВЫХОДОМ ИЗ АККАУНТА)')

def test_login_with_lcard(driver):
    print('НАЧАЛО ПРОВЕРКИ ВХОДА С КАРТОЙ ЛОЯЛЬНОСТИ (С ВЫХОДОМ ИЗ АККАУНТА)')

    try:
        # Вход по карте лояльности
        login_page = Login_account(driver)
        loyalty_card = "4887444077419141"
        password = "*+1M^Fkl"
        login_page.login_with_lcard(loyalty_card, password)
        login_page.logout()

        # Добавьте проверки после входа, если необходимо


    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

    finally:
        print('ОКОНЧАНИЕ ПРОВЕРКИ ВХОДА С КАРТОЙ ЛОЯЛЬНОСТИ (С ВЫХОДОМ ИЗ АККАУНТА)')