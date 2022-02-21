import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_page_contains_add_to_cart_button(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(30) 
    button = browser.find_elements_by_css_selector("a.btn-default:nth-child(1)")
    assert button, '!!!НЕ НАШЕЛ КОРЗИНУ!!!'
    
     # button = len(browser.find_elements_by_css_selector("a.btn-default:nth-child(1)"))
     # assert button > 0, '!!!НЕ НАШЕЛ КОРЗИНУ!!!'
    
    