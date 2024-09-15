import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    # driver = webdriver.Chrome()
    # url = 'https://www.saucedemo.com/'
    # self.driver.get(self.url)
    # self.driver.maximize_window()

    yield

    # driver.quit()
    print("Finish test")

@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")