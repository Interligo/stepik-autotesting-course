import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert add_to_basket_button is not None, 'Button not found.'
