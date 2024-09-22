import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.maine_page import Maine_page

import time
from faker import Faker

from utilites.Logger import Logger


class Registration_page(Maine_page):

    def create_user(self):
        fake = Faker('ru_RU')
        fname = fake.first_name()
        lname = fake.last_name()
        phone = fake.numerify(text='79#########')
        lcard = fake.credit_card_number()
        email = fake.email()
        passw = fake.password(8)
        user = User(fname, lname, phone, lcard, email, passw)
        print(user)
        return user

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    first_name = '//input[@id="elm_6"]'
    last_name = '//input[@id="elm_7"]'
    phone = '//input[@id="elm_9"]'
    loyalty_card = '//input[@id="elm_42"]'
    email = '//input[@id="email"]'
    password = '//input[@id="password1"]'
    repeat_password = '//input[@id="password2"]'
    agreement = '//input[@id="user_data_52_check_pd"]'
    agreement2 = '//input[@id="gdpr_agreements_user_registration"]'
    registration_button = '//button[@name="dispatch[profiles.update]"]'
    registration_success = '//h1[@class="ty-mainbox-title"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_loyalty_card(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loyalty_card)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_repeat_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.repeat_password)))

    def get_agreement(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.agreement)))

    def get_agreement2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.agreement2)))

    def get_registration_button(self):
        registration_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.registration_button))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", registration_button)
        return registration_button

    def get_registration_success(self):
        registration_success = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.registration_success))
        )
        return registration_success

    # Actions
    def input_first_name(self, user, fname=None):
        fname = fname if fname is not None else user.fname
        self.get_first_name().send_keys(fname)
        print("Ввод имени")

    def input_last_name(self, user, lname=None):
        lname = lname if lname is not None else user.lname
        self.get_last_name().send_keys(lname)
        print("Ввод фамилии")

    def input_phone(self, user, phone=None):
        phone = phone if phone is not None else user.phone
        self.get_phone().send_keys(phone)
        print("Ввод телефона")

    def input_loyalty_card(self, user, lcard=None):
        lcard = lcard if lcard is not None else user.lcard
        self.get_loyalty_card().send_keys(lcard)
        print("Ввод карты лояльности")

    def input_email(self, user, email=None):
        email = email if email is not None else user.email
        self.get_email().send_keys(email)
        print("Ввод email")

    def input_password(self, user, passw=None):
        passw = passw if passw is not None else user.passw
        self.get_password().send_keys(passw)
        print("Ввод пароля")

    def input_repeat_password(self, user, passw=None):
        passw = passw if passw is not None else user.passw
        self.get_repeat_password().send_keys(passw)
        print("Повторный ввод пароля")

    def click_agreement(self):
        self.get_agreement().click()
        print("Согласие №1")

    def click_agreement2(self):
        self.get_agreement2().click()
        print("Согласие №2")

    def click_registration_button(self):
        registration_button = self.get_registration_button()
        registration_button.click()
        print("Нажатие кнопки регистрации")

    # Methods
    def register_user(self, user, fname=None, lname=None, phone=None, lcard=None, email=None, passw=None):
        with allure.step("Register user"):
            Logger.add_start_step(method='register_user')
            """ Регистрация пользователя """
            self.to_registration()  # Переход к странице регистрации
            # self.driver.get(self.url)
            self.driver.maximize_window()
            time.sleep(3)
            self.input_first_name(user, fname)
            self.input_last_name(user, lname)
            self.input_phone(user, phone)
            self.input_loyalty_card(user, lcard)
            self.input_email(user, email)
            self.input_password(user, passw)
            self.input_repeat_password(user, passw)
            time.sleep(2)
            self.click_agreement()
            self.click_agreement2()
            time.sleep(2)
            self.click_registration_button()
            time.sleep(5)
            self.assert_url("https://100sistem.ru/index.php?dispatch=profiles.success_add")
            self.assert_word(self.get_registration_success(), "Вы успешно зарегистрированы")
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='register_user')


class User:
    def __init__(self, fname=None, lname=None, phone=None, lcard=None, email=None, passw=None):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.lcard = lcard
        self.email = email
        self.passw = passw

    def __str__(self):
        return f"User(fname={self.fname}, lname={self.lname}, phone={self.phone}, lcard={self.lcard}, email={self.email}, passw={self.passw})"

