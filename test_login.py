from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()
driver.save_screenshot("result.png")


username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
password.send_keys("wrongpassword")

login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

time.sleep(2)

message = driver.find_element(By.ID, "flash").text
print("Message:", message)

driver.quit()