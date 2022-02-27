from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

link = (By.CSS_SELECTOR, '#masthead .flex-col.hide-for-medium.flex-left.flex-grow > ul')
link_categories = (By.CSS_SELECTOR, 'li[id *= "menu-item-"] a[href *= "https://gettop.us/product-category/"]')
selected_products = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')





@when('Click through categories on top menu')
def click_categories_menu(context):
    context.driver.find_element(*link).click()
    sleep(5)


@then('Verify correct pages are open')
def verify_each_element(context):
    expected_categories = ['MAC', 'IPHONE', 'IPAD', 'WATCH', 'ACCESSORIES']

    for i in range(len(expected_categories)):
        context.driver.find_elements(*link_categories)[i].click()
        actual_category = context.driver.find_elements(*link_categories)[i].text

        assert actual_category in expected_categories[i], f'Expected {expected_categories[i]}, but got {actual_category}'

# @then('Verify correct pages are open')
# def verify_each_element(context):
#     expected_categories = ['MAC', 'IPHONE', 'IPAD', 'WATCH', 'ACCESSORIES']
#
#     categories = context.driver.find_elements(*link_categories)
#     for i in range(len(categories)):
#         categories[i].click()
#         actual_category = context.driver.find_elements(*selected_products).text()
#
#         assert actual_category == expected_categories[i], f'Expected {expected_categories[i]}, but got {actual_category}'
#
