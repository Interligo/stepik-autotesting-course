from selenium import webdriver
import time
import os


file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lesson2.2_step8_upload_file.txt")

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        pass

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет все поля
    input_first_name = browser.find_element_by_name("firstname").send_keys("Ivan")
    input_last_name = browser.find_element_by_name("lastname").send_keys("Petrov")
    input_email = browser.find_element_by_name("email").send_keys("Petrov@mail.ru")
    send_file = browser.find_element_by_id("file").send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
