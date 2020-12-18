import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope='function')
def answer() -> str:
    delay = 2.3  # Задержка локального компьютера
    return str(math.log(int(time.time() + delay)))


class TestLinks:
    @classmethod
    def setup_class(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    @pytest.mark.parametrize('link', links)
    def test_link(self, link, answer):
        self.browser.get(link)
        # Ожидает появления элемента с тегом "textarea"
        textarea = WebDriverWait(self.browser, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
        textarea.send_keys(answer)
        self.browser.find_element_by_css_selector('button.submit-submission').click()
        feedback = self.browser.find_element_by_css_selector('pre.smart-hints__hint').text

        try:
            assert 'Correct!' == feedback
        except AssertionError:
            with open('lesson3_6_step3_parametrize_test.py_errors.log', 'a') as f:
                f.write(feedback)
            raise AssertionError('Test failed! Check errors log file.')
