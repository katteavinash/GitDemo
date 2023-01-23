import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("Users/Avinash Katte/Downloads/chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("Br")
results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(results)
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)
time.sleep(5)