from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет все поля
    input_first_name = browser.find_element_by_css_selector(".first_class [placeholder='Input your first name']")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_css_selector(".second_class [placeholder='Input your last name']")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element_by_css_selector(".third_class [placeholder='Input your email']")
    input_email.send_keys("Petrov@mail.ru")
    input_phone_number = browser.find_element_by_css_selector(".first_class [placeholder='Input your phone:']")
    input_phone_number.send_keys("89771335588")
    input_address = browser.find_element_by_css_selector(".second_class [placeholder='Input your address:']")
    input_address.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
