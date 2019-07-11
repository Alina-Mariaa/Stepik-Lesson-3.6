import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_should_have_basket_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form")
