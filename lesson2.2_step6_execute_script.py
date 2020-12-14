from selenium import webdriver
import time
import math


def calc(x: int) -> str:
    """Функция для вычисления задачи по ссылке."""
    result = str(math.log(abs(12 * math.sin(x))))
    return result


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Скриллим страницу вниз
    browser.execute_script("window.scrollBy(0, 150);")

    # Ищем значение х
    element_x = browser.find_element_by_id("input_value").text

    # Вычисляем значение
    answer = calc(int(element_x))

    # Вводим вычисленный ответ в необходимое поле
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)

    # Отмечаем необходимые поля
    elements_to_select = ("robotCheckbox", "robotsRule")
    for element in elements_to_select:
        browser.find_element_by_id(element).click()

    # Отправляем результат
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
