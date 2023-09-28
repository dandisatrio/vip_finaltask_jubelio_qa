from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://app.jubelio.com/login"

driver.get(url)
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(100)
print(driver.title) 
print(driver.current_url)
driver.close()

