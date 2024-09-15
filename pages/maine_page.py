import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from base.base_cl import Base


class Maine_page(Base):
    url = 'https://100sistem.ru/'

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    account = '//i[@class="ut2-icon-outline-account-circle"]'
    account_reg = '//a[@class="ty-btn ty-btn__primary"]'
    account_enter = '//a[@data-ca-target-id="login_block851"]'
    button_logout = '//a[@class ="ty-btn ty-btn__primary"]'
    all_products = '//a[@class="ty-menu__item-link a-first-lvl childs"]'
    all_products_more = '//a[@class="ut2-more"]'
    mixers = '//a[.//span[contains(text(), "Смесители")]]'

    # Getters
    def get_account(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.account)))

    def get_account_reg(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.account_reg)))

    def get_account_enter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.account_enter)))

    def get_button_logout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_logout)))

    def get_all_products(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.all_products)))

    def get_all_products_more(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.all_products_more)))

    def get_mixers(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mixers)))

    # Actions
    def click_account(self):
        self.get_account().click()
        print("Нажатие иконки аккаунта")

    def click_account_reg(self):
        self.get_account_reg().click()
        print("Нажатие регистрации в аккаунте")

    def click_account_enter(self):
        self.get_account_enter().click()
        print("Нажатие войти в аккаунте")

    def click_button_logout(self):
        self.get_button_logout().click()
        print("Нажатие выйти из аккаунта")

    def move_all_products(self):
        all_products_element = self.get_all_products()
        actions = ActionChains(self.driver)
        actions.move_to_element(all_products_element).perform()
        print("Наведение курсора на 'Все товары'")

    def move_all_products_more(self):
        all_products_more = self.get_all_products_more()
        actions = ActionChains(self.driver)
        actions.move_to_element(all_products_more).perform()
        print("Наведение курсора на элемент в 'еще' после наведения на 'Все товары'")

    def click_mixers(self):
        faucets_element = self.get_mixers()
        faucets_element.click()
        print("Нажатие на 'Смесители' в разделе 'Все товары, еще'")

    # Methods
    def to_registration(self):
        """ Переход к странице регистрации"""
        self.driver.get(self.url)  # Добавлен переход на URL
        self.get_current_url()
        self.click_account()
        self.click_account_reg()

    def to_entrance(self):
        """ Авторизация пользователя"""
        self.driver.get(self.url)  # Добавлен переход на URL
        self.get_current_url()
        self.click_account()
        self.click_account_enter()

    def logout(self):
        """ Выход из аккаунта"""
        self.click_account()
        self.assert_word(self.get_button_logout(), 'Выйти')
        self.click_button_logout()

    def to_mixers(self):
        """ Переход к смесителям  с основной страницы (Все товары - еще - смесители)"""
        self.move_all_products()
        time.sleep(3)
        self.move_all_products_more()
        time.sleep(3)
        self.click_mixers()
        time.sleep(3)

# Вы успешно зарегистрированы
# < h1
# class ="ty-mainbox-title" >
# Вы
# успешно
# зарегистрированы
# < / h1 >
# https://100sistem.ru/index.php?dispatch=profiles.success_add
