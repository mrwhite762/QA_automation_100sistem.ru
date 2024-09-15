import time

import pytest
from selenium import webdriver

from pages.login_pag import Login_account
from pages.mixer_list import Mixer_list
from pages.placing_order import Placing_order

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_critical_path(driver):
    print('НАЧАЛО ПРОВЕРКИ')

    try:
        # Вход по email
        login_page = Login_account(driver)
        email = "kudrjavtsevzinovi@example.org"
        password = "*+1M^Fkl"
        login_page.login_with_email(email, password)
        time.sleep(3)
        login_page.to_mixers()

        # Создаем экземпляр Mixer_list и вызываем метод selection_mixer
        mixer_list_page = Mixer_list(driver)
        mixer_list_page.selection_mixer()

        placing_order_page = Placing_order(driver)
        placing_order_page.place_order()

        # Добавьте проверки после входа, если необходимо

    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

    finally:
        print('ОКОНЧАНИЕ ПРОВЕРКИ')

