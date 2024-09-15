import datetime

class Base:

    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'URL сайта: "{get_url}"')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert result in value_word, f"ТЕКСТ: '{value_word}' НЕ СОДЕРЖИТ ОЖИДАЕМОГО: '{result}'"
        print(f'ТЕКСТ: "{value_word}" СОДЕРЖИТ ОЖИДАЕМЫЙ: "{result}"')

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f'URL "{get_url}" совпадает с проверяемым')
