import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.globals import Globals
from pages.maine_page import Maine_page
from utilites.Logger import Logger


class Mixer_list(Maine_page):
    url = 'https://100sistem.ru/santehnika/smesiteli/'

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    brand = '//div[@id="sw_content_192_14"]'
    brand_search = '//input[@id="elm_search_192_14"]'
    brand_dorff = '//label[@for="elm_checkbox_192_14_1542"]'
    price = '//div[@id="sw_content_189_13"]'
    price_limit_max = '//input[@id="slider_189_13_right"]'
    mixer_D1002100 = '//a[@title="D1002100 Norma смеситель для умывальника"]'
    mixer_D1002100_price = '//span[@id="sec_discounted_price_10583"]'
    add_cart = '//button[@id="button_cart_10583"]'
    order = '//a[@class="ty-btn ty-btn__primary cm-notification-close "]'

    # Getters
    def get_brand(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_brand_search(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_search)))

    def get_brand_dorff(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_dorff)))

    def get_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_price_limit_max(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_limit_max)))

    """При прокрутке к элементу поисковая строка начинает его закрывать, поэтому останавливаемся немного выше"""
    def get_mixer_D1002100(self):
        mixer_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.mixer_D1002100))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", mixer_element)
        self.driver.execute_script("window.scrollBy(0, -100);")  # Смещение вверх на 100 пикселей
        return mixer_element


    def get_mixer_D1002100_price(self):
        price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.mixer_D1002100_price))
        )
        return price_element.text

    def get_add_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_cart)))

    def get_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order)))

    # Actions
    def click_brand(self):
        self.get_brand().click()
        print("Нажатие список брендов")

    def input_brand_search(self):
        search_text = "Dorff"
        search_input_element = self.get_brand_search()
        search_input_element.clear()
        search_input_element.send_keys(search_text)
        print(f"Ввод текста '{search_text}' в поисковую строку брендов")

    def click_brand_dorff(self):
        self.get_brand_dorff().click()
        print("Выбор бренда 'Dorff'")

    def click_price(self):
        self.get_price().click()
        print("Нажатие 'Цена'")

    def input_price_limit_max(self):
        price_text = "6000"
        price_input_element = self.get_price_limit_max()
        price_input_element.clear()
        price_input_element.send_keys(price_text)
        print(f"Ввод максимальной цены '{price_text}'")

    def click_mixer_D1002100(self):
        Globals.set_price_mixer_D1002100(self.get_mixer_D1002100_price())
        print(f"Цена товара mixer_D1002100 установлена в глобальную переменную: {Globals.price_mixer_D1002100}")
        self.get_mixer_D1002100().click()
        print("Переход в карточку смесителя")

    def click_add_cart(self):
        self.get_add_cart().click()
        print("Товар добавляется в корзину")

    def click_order(self):
        self.get_order().click()
        print("Оформить заказ")

    # Methods
    def selection_mixer(self):
        with allure.step("Selection mixer"):
            Logger.add_start_step(method='selection_mixer')
            """ выбор смесителя"""
            self.driver.get(self.url)
            self.get_current_url()
            self.driver.maximize_window()
            self.click_brand()
            time.sleep(2)
            self.input_brand_search()
            time.sleep(2)
            self.click_brand_dorff()
            time.sleep(5)
            self.assert_url("https://100sistem.ru/santehnika/smesiteli/dorff/")
            self.click_price()
            time.sleep(2)
            self.input_price_limit_max()
            time.sleep(5)
            self.click_mixer_D1002100() # переход в карточку + запись в глобальную переменную
            time.sleep(2)
            self.click_add_cart()
            time.sleep(3)
            self.click_order()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='selection_mixer')
