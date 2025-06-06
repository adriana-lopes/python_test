import data
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class TestUrbanRoutes:

@classmethod
    def setup_class(cls):

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(5)


    def test_set_route(self):
        self.page.set_address()

    def test_select_plan(self):


    def test_fill_phone_number(self):


    def test_fill_card(self):


    def test_comment_for_driver(self):


    def test_order_blanket_and_handkerchiefs(self):


    def test_order_2_ice_creams(self):
        for i in range(2):


    def test_car_search_model_appears(self):

    @classmethod
def teardown_class(cls)
        cls.driver.quit()