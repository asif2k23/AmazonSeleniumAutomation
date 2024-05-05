from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

try:
    time.sleep(20)   #For captcha
    search_dropdown = driver.find_element(By.ID,"searchDropdownBox")
    search_dropdown.click()

    baby_options = driver.find_element(By.XPATH,"//*[@id='searchDropdownBox']/option[text()='Baby']")
    baby_options.click()

    search_input = driver.find_element(By.ID,"twotabsearchtextbox")
    search_input.send_keys("bag")
    time.sleep(2)

    search_button = driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']")
    search_button.click()

finally:
    time.sleep(2)
    driver.quit()