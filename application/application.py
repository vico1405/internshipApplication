from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResults
# from pages.product_result import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header

        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
#        self.product_result = ProductPage(self.driver)
