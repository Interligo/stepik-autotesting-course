import time
import math
from selenium import webdriver


links_list = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
              'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
              'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']

secret_phrase = []

for link in links_list:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    answer = math.log(int(time.time() + 2.3))  # Задержка локального компьютера

    send_answer = browser.find_element_by_css_selector('.textarea').send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector('.submit-submission').click()

    find_text_from_page = browser.find_element_by_css_selector('.smart-hints__hint')
    text = find_text_from_page.text

    browser.quit()

    # Сбор секретной фразы по частям
    if text != 'Correct!':
        secret_phrase.append(text)

    # assert 'Correct!' == text

print(secret_phrase)
