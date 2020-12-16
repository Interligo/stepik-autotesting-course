from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значения чисел
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    num_sum = int(num1) + int(num2)

    # Выбираем нужное значение в выпадающем списке
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(num_sum))

    # Отправляем результат
    button = browser.find_element_by_class_name("btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
