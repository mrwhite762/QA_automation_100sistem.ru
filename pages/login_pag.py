import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

from pages.registration_page import User
from pages.maine_page import Maine_page
from utilites.Logger import Logger


class Login_account(Maine_page, User):
    def __init__(self, driver):
        super().__init__(driver)
        self.maine_page = Maine_page(driver)  # Создаем экземпляр класса Maine_page

    # Locators
    email_or_lcard = '//input[@id="login_popup851"]'
    password = '//input[@id="psw_popup851"]'
    enter_button = '//button[@name="dispatch[auth.login]"]'

    # Getters
    def get_email_or_lcard(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_or_lcard)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # Actions
    def input_email(self, user_or_email, email=None):
        if isinstance(user_or_email, str):
            email = user_or_email
        else:
            email = user_or_email.email
        self.get_email_or_lcard().send_keys(email)
        print("Ввод email")

    def input_lcard(self, user_or_lcard, lcard=None):
        if isinstance(user_or_lcard, str):
            lcard = user_or_lcard
        else:
            lcard = user_or_lcard.lcard
        self.get_email_or_lcard().send_keys(lcard)
        print("Ввод карты лояльности")

    def input_password(self, user_or_passw, passw=None):
        if isinstance(user_or_passw, str):
            passw = user_or_passw
        else:
            passw = user_or_passw.passw
        self.get_password().send_keys(passw)
        print("Ввод пароля")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Нажатие кнопки входа")

    # Methods
    def login_with_email(self, email, password):
        with allure.step("Login with email"):
            Logger.add_start_step(method='login_with_email')
            self.maine_page.to_entrance()
            self.driver.maximize_window()
            time.sleep(3)
            self.input_email(email)
            self.input_password(password)
            time.sleep(3)
            self.click_enter_button()
            time.sleep(5)
            # self.assert_url("https://100sistem.ru/index.php?dispatch=auth.login_form")
            print("Успешный вход по email")
            Logger.add_end_step(url=self.driver.current_url, method='login_with_email')

    def login_with_lcard(self, loyalty_card, password):
        with allure.step("Login with lcard"):
            Logger.add_start_step(method='login_with_lcard')
            self.maine_page.to_entrance()
            self.driver.maximize_window()
            time.sleep(3)
            self.input_lcard(loyalty_card)
            self.input_password(password)
            time.sleep(3)
            self.click_enter_button()
            time.sleep(5)
            # self.assert_url("https://100sistem.ru/index.php?dispatch=auth.login_form")
            print("Успешный вход по карте лояльности")
            Logger.add_end_step(url=self.driver.current_url, method='login_with_lcard')
