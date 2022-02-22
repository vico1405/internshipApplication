from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import Page


class Header(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, 'i.icon-search')
    SEARCH_INPUT = (By.ID, 'woocommerce-product-search-field-0')


    def hover_products(self):
            SEARCH_ICON = self.find_element(*self.SEARCH_ICON)
            hover = ActionChains(self.driver)
            hover.move_to_element(SEARCH_ICON)
            hover.perform()

    def search_input(self, text):
        self.input_text(text, *self.SEARCH_INPUT)


