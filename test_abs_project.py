# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
#
# def test_exception1():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element(By.CSS_SELECTOR, "button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally:
#         browser.quit()
#
# def test_exception2():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally:
#         browser.quit()



# from selenium import webdriver
#
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# class TestMainPage1():
#
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite 1 ..")
#         self.browser = webdriver.Chrome()
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite 1 ..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         print('start test link 1')
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         print('start test basket 1')
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#
#
# class TestMainPage2():
#
#     def setup_method(self):
#         print("start browser for test 2..")
#         self.browser = webdriver.Chrome()
#
#     def teardown_method(self):
#         print("quit browser for test 2..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         print('start test link 2')
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         print('start test basket 2')
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")




# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")






# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         print("start test1")
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#         print("finish test1")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         print("start test2")
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#         print("finish test2")





# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")
#
#
# class TestMainPage1():
#     def test_guest_should_see_login_link(self, browser):
#         # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")




# import pytest
#
#
# @pytest.fixture(scope="class")
# def prepare_faces():
#     print("^_^", "\n")
#     yield
#     print(":3", "\n")
#
#
# @pytest.fixture()
# def very_important_fixture():
#     print(":)", "\n")
#
#
# @pytest.fixture(autouse=True)
# def print_smiling_faces():
#     print(":-Р", "\n")
#
#
# class TestPrintSmilingFaces():
#     def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
#         print("finish test1")
# # какие-то проверки
#
#     def test_second_smiling_faces(self, prepare_faces):# какие-то проверки
#         print("finish test1")
#
#



# маркировка

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     @pytest.mark.regression
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#



# две маркировки в одном тесте
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1:
#
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     @pytest.mark.smoke
#     @pytest.mark.win10
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")




# пропуск теста
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     @pytest.mark.skip
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")








# МАРКИРОВКА ПАДАЮЩЕГО ТЕСТА

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "button.favorite")



# ПАДАЮЩИЙ ТЕСТ КОТОРЫЙ В КОНСОЛИ ВИДЕН (pytest -rx -v  test_abs_project.py)
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "button.favorite")


# XPASS-тесты ( pytest -rX -v test_abs_project.py ) - подробное описание в консоли
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")




# ЗАДАНИЕ





#
# import pytest
#
#
# class TestMainPage():
#     # номер 1
#     @pytest.mark.xfail
#     @pytest.mark.smoke
#     def test_guest_can_login(self, browser):
#         assert True
#
#     # номер 2
#     @pytest.mark.regression
#     def test_guest_can_add_book_from_catalog_to_basket(self, browser):
#         assert True
#
#
# class TestBasket():
#     # номер 3
#     @pytest.mark.skip(reason="not implemented yet")
#     @pytest.mark.smoke
#     def test_guest_can_go_to_payment_page(self, browser):
#         assert True
#
#     # номер 4
#     @pytest.mark.smoke
#     def test_guest_can_see_total_price(self, browser):
#         assert True
#
#
# @pytest.mark.skip
# class TestBookPage():
#     # номер 5
#     @pytest.mark.smoke
#     def test_guest_can_add_book_to_basket(self, browser):
#         assert True
#
#     # номер 6
#     @pytest.mark.regression
#     def test_guest_can_see_book_price(self, browser):
#         assert True
#
#
# # номер 7
# @pytest.mark.beta_users
# @pytest.mark.smoke
# def test_guest_can_open_gadget_catalogue(browser):
#     assert True


# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")


# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")


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







