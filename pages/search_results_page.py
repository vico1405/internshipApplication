from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResults(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, 'i.icon-search')
    SEARCH_INPUT = (By.ID, 'woocommerce-product-search-field-0')
    PRODUCT_RESULTS = (By.CSS_SELECTOR, "div[data-index='1']")


    def hover_products(self):
        self.hover_products()

    def input_element(self, text, *locator):
        self.input_text(text,*locator)

    def click_element(self,*locator):
        self.click(*locator)

    def verify_product_result(self):
        self.verify_url_contains_query('ipad')