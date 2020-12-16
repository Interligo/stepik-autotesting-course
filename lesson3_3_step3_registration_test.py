import pytest
from selenium import webdriver


class TestRegistration:
    def open_browser(self):
        self.browser = webdriver.Chrome()

    def close_browser(self):
        self.browser.quit()

    def fill_form(self, url):
        self.open_browser()
        self.browser.get(url)

        input_first_name = self.browser.find_element_by_css_selector\
            (".first_class [placeholder='Input your first name']").send_keys("Ivan")
        input_last_name = self.browser.find_element_by_css_selector\
            (".second_class [placeholder='Input your last name']").send_keys("Petrov")
        input_email = self.browser.find_element_by_css_selector\
            (".third_class [placeholder='Input your email']").send_keys("Petrov@mail.ru")
        input_phone_number = self.browser.find_element_by_css_selector\
            (".first_class [placeholder='Input your phone:']").send_keys("89771335588")
        input_address = self.browser.find_element_by_css_selector\
            (".second_class [placeholder='Input your address:']").send_keys("Russia")
        button = self.browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.close_browser()
        return welcome_text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)
        assert "Congratulations! You have successfully registered!" == registration_result

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fill_form(link)
        assert "Congratulations! You have successfully registered!" == registration_result


if __name__ == "__main__":
    pytest.main()
