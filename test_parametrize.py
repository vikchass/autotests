import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage:
    @pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, link):
        link = f"https://stepik.org/lesson/{link}/step/1"
        ans = str(math.log(int(time.time())))
        browser.get(link)
        time.sleep(10)
        # ищем поле и заполняем его
        pole = browser.find_element(By.TAG_NAME, "textarea")
        pole.send_keys(ans)
        # ждем когда кнопка станет активной и жмем на нее
        button = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
                )
        button.click()
        time.sleep(3)
        chtxt = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        assert "Correct!" in chtxt.text

