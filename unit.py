import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time




class StepikTest(unittest.TestCase):

    def test_1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.first_class > input.first")
        input1.send_keys("Ivan")
        self.assertEqual(input1.get_attribute("value"), "Ivan", "текст должен содержать Ivan")
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

        time.sleep(10)
        browser.quit()

    def test_2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.first_class > input.first")
        input1.send_keys("Ivan")
        self.assertEqual(input1.get_attribute("value"), "Ivan", "текст должен содержать Ivan")
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
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()

