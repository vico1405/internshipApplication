from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_ICON = (By.CSS_SELECTOR, 'i.icon-search')
SEARCH_INPUT = (By.ID, 'woocommerce-product-search-field-0')
PRODUCT_RESULTS = (By.CSS_SELECTOR, "div[data-index='1']")

@given('Open gettop page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')

@when('Hover over product options')
def hover_products(context):
    context.app.header.hover_products()


@when('Search for iPad')
def input_ipad(context):
    context.app.search_results_page.input_element('iPad', *SEARCH_INPUT)
#   context.driver.find_element(By.ID, 'woocommerce-product-search-field-0]').send_keys('iPad')
#    context.app.search_results_page.verify_product_result(expected_text='iPad')
    context.app.search_results_page.click_element(*PRODUCT_RESULTS)
    from time import sleep
    sleep(5)

@then('Product result for iPad are shown')
def verify_found_results_text(context):
    context.app.search_results_page.verify_product_result()

