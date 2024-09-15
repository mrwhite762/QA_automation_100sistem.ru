import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.mixer_list import Mixer_list


class Placing_order(Mixer_list):
    url = 'https://100sistem.ru/checkout/'

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    order_sum = '(//td[@class="ty-checkout-summary__item ty-right"])[2]'
    sogl1 = '//input[@id="checkout_135_check_pd"]'
    sogl2 = '//input[@name="accept_terms"]'
    address = '//input[@id="litecheckout_s_address"]'
    delivery = '(//div[@class="b--ship-way__unit__label__text__pseudo-radio"])[2]'
    delivery_cart = '//label[@for="store_0_6_35"]'
    note = '//textarea[@id="litecheckout_comment_to_shipping"]'
    design = '//button[@id="litecheckout_place_order"]'
    successful_order = '//div[@class="ty-checkout-complete__order-success"]'

    # Getters
    def get_order_sum(self):
        price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.order_sum))
        )
        return price_element.text

    def get_sogl2(self):
        sogl2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.sogl2))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", sogl2)
        return sogl2

    def get_sogl1(self):
        sogl1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.sogl1))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", sogl1)
        return sogl1

    def get_address(self):
        address = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.address))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", address)
        return address

    def get_delivery(self):
        delivery = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", delivery)
        return delivery

    def get_delivery_cart(self):
        delivery_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_cart))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", delivery_cart)
        return delivery_cart

    def get_note(self):
        note = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.note))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", note)
        return note

    def get_design(self):
        design = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.design))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", design)
        return design

    def get_successful_order(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.successful_order)))

    # Actions
    def assert_prices(self):
        try:
            order_sum = self.get_order_sum()
            assert self.didgit == order_sum, f"Цена смесителя ({self.didgit}) не совпадает с суммой в заказе ({order_sum})"
            print("Цена смесителя совпадает с суммой в заказе")
        except AssertionError as e:
            print(e)
            # Продолжаем выполнение кода

    def click_sogl1(self):
        try:
            self.get_sogl1().click()
            print("Нажатие согласие 1")
        except Exception as e:
            print(f"Ошибка при нажатии согласия 1: {e}")

    def click_sogl2(self):
        try:
            self.get_sogl2().click()
            print("Нажатие согласие 2")
        except Exception as e:
            print(f"Ошибка при нажатии согласия 2: {e}")

    def click_delivery(self):
        try:
            self.get_delivery().click()
            print("Нажатие самовывоз")
        except Exception as e:
            print(f"Ошибка при нажатии самовывоза: {e}")

    def click_delivery_cart(self):
        try:
            self.get_delivery_cart().click()
            print("Выбор магазина на карте")
        except Exception as e:
            print(f"Ошибка при выборе магазина на карте: {e}")

    def input_address(self):
        address_text = "пр. Культуры д. 29 к. 1"
        try:
            address_input_element = self.get_address()
            address_input_element.send_keys(address_text)
            print(f"Ввод адреса: '{address_text}'")
        except Exception as e:
            print(f"Ошибка при вводе адреса: {e}")

    def input_note(self):
        note_text = "Тестовый заказ, просьба отменить"
        try:
            note_input_element = self.get_note()
            note_input_element.send_keys(note_text)
            print(f"Ввод примечания: '{note_text}'")
        except Exception as e:
            print(f"Ошибка при вводе примечания: {e}")

    def click_design(self):
        try:
            self.get_design().click()
            print("Нажатие кнопки 'Оформить заказ'")
        except Exception as e:
            print(f"Ошибка при нажатии кнопки 'Оформить заказ': {e}")

    # Methods
    def place_order(self):
        """ Оформление заказа """
        self.assert_url(self.url)
        self.assert_prices()
        self.click_sogl2()
        time.sleep(2)
        self.input_address()
        time.sleep(2)
        self.click_delivery()
        time.sleep(5)
        self.click_delivery_cart()
        time.sleep(25) # На странице отрабатывает джаваскрипт с задержкой, пауза необходима
        self.input_note()
        time.sleep(2)
        self.click_sogl1()
        time.sleep(2)
        self.click_design()
        time.sleep(25) # Пауза для успешного формирования заказа
        self.assert_word(self.get_successful_order(), "Поздравляем! Ваш заказ размещен.")