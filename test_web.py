# def test_input_text(expected_result, actual_result):
#    assert expected_result == actual_result, \
#     f"expected {expected_result}, got {actual_result}"


# def test_substring(full_string, substring):
#     assert substring in full_string, \
# f"expected '{substring}' to be substring of '{full_string}'"


# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/ html / body / div / form / div[1] / div[3] / input")
    input3.send_keys("ggg@mail.ru")
    input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("77777777777")
    input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
