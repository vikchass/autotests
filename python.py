# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(5)
#
#     browser.quit()


# ПРОВЕРЯЕМ ЧТО ПОЛЯ ВАЛИДНО ЗАПОЛНЕНЫ

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#
# ТЕСТ ПАДАЕТ С ОШЩИБКОЙ
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/registration2.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "/ html / body / div / form / div[1] / div[3] / input")
#     input3.send_keys("ggg@mail.ru")
#     input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
#     input4.send_keys("77777777777")
#     input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
#     input5.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "/html/body/div/form/button")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/registration2.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "/ html / body / div / form / div[1] / div[3] / input")
#     input3.send_keys("ggg@mail.ru")
#     input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
#     input4.send_keys("77777777777")
#     input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
#     input5.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "/html/body/div/form/button")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# СЛОЖНОЕ ЗАДАНИЕ
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# import time
# import math


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# link = "https://suninjuly.github.io/math.html"

# try:
#     browser: WebDriver = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#
#     x = browser.find_element(By.CSS_SELECTOR, "#answer")
#     x.send_keys(y)
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     option1.click()
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     option1.click()
#
#     button = browser.find_element(By.XPATH, "/html/body/div/form/button")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()



# ОООООЧЕН СЛОЖНОЕ ЗАДАНИЕ

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# link = "http://suninjuly.github.io/get_attribute.html"
#
# try:
#     browser: WebDriver = webdriver.Chrome()
#     browser.get(link)
#     x = browser.find_element(By.CSS_SELECTOR, "#treasure")
#     x = x.get_attribute("valuex")
#     y = calc(x)
#
#     x = browser.find_element(By.CSS_SELECTOR, "#answer")
#     x.send_keys(y)
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     option1.click()
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     option1.click()
#
#     button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
#     button.click()
#
#
# finally:
#     time.sleep(10)
#     browser.quit()



#FFF (раскрывающийся список, поиск по видимому значению

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# import time
#
#
# def calc(y, o):
#     return int(y) + int(o)
#
#
# link = "http://suninjuly.github.io/selects1.html"
#
# try:
#     browser: WebDriver = webdriver.Chrome()
#     browser.get(link)
#
#     a = browser.find_element(By.CSS_SELECTOR, "#num1")
#     b = browser.find_element(By.CSS_SELECTOR, "#num2")
#     y = a.text
#     o = b.text
#     x = calc(y, o)
#     print(x)

#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(x))
#
#     button = browser.find_element(By.XPATH, "/html/body/div/form/button")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()
#




# СКРОЛЛ

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#
# link = "http://SunInJuly.github.io/execute_script.html"
#
# try:
#     browser: WebDriver = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#
#     x = browser.find_element(By.CSS_SELECTOR, "#answer")
#     x.send_keys(y)
#
#     option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     option1.click()
#
#     radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
#     radio.click()
#
#     button = browser.find_element(By.XPATH, "/html/body/div/form/button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
#
# finally:
#     time.sleep(10)
#     browser.quit()




# ФАЙЛ

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
#
#
# link = "http://suninjuly.github.io/file_input.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
#     input3.send_keys("ggg@mail.ru")
#
#     button1 = browser.find_element(By.CSS_SELECTOR, "#file")
#     current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#     file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#     button1.send_keys(file_path)
#
#     button2 = browser.find_element(By.XPATH, "/html/body/div/form/button")
#     button2.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()




# Модалка где есть согласие и отказ
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# link = "http://suninjuly.github.io/alert_accept.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
#     button.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#
#     x = browser.find_element(By.CSS_SELECTOR, "#answer")
#     x.send_keys(y)
#
#     button2 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
#     button2.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()




# Переход на новую вкладку

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# link = "http://suninjuly.github.io/redirect_accept.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
#     button.click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#
#     x = browser.find_element(By.CSS_SELECTOR, "#answer")
#     x.send_keys(y)
#
#     button2 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
#     button2.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()



#  ОЖИДАНИЕ (плохое)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# link = "http://suninjuly.github.io/wait1.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     time.sleep(1)
#
#     button = browser.find_element(By.ID, "verify")
#     button.click()
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text
#
# finally:
#     time.sleep(10)
#     browser.quit()




#  ОЖИДАНИЕ (хорошее)- не явное

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# link = "http://suninjuly.github.io/wait1.html"
#
# try:
#     browser = webdriver.Chrome()
#
#     browser.implicitly_wait(5)   # говорим WebDriver искать каждый элемент в течение 5 секунд
#
#     browser.get(link)
#
#     button = browser.find_element(By.ID, "verify")
#     button.click()
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text
#
# finally:
#     time.sleep(10)
#     browser.quit()


#  ОШИБКА
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# link = "http://suninjuly.github.io/cats.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element(By.ID, "button")
#     browser.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()




#  ОЖИДАНИЕ (хорошее)- явное

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
#
# link = "http://suninjuly.github.io/wait2.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = WebDriverWait(browser, 5).until(   # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

    ##! говорим Selenium проверять в течение 5 секунд пока кнопка станет НЕактивной
    ## button = WebDriverWait(browser, 5).until_not(
    ##     EC.element_to_be_clickable((By.ID, "verify"))
    ## )

#     button.click()
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text
#
# finally:
#     time.sleep(10)
#     browser.quit()



#  ОЖИДАНИЕ (хорошее)- явное2

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    x_el= browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_el.text
    y = calc(x)

    x = browser.find_element(By.CSS_SELECTOR, "#answer")
    x.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()




