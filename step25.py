from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(15)
    browser.quit()
