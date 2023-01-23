from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("Users/Avinash Katte/Downloads/chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggielist = driver.find_elements(By.XPATH, "//td[1]")
sortedveggies = []
for veg in veggielist:
    sortedveggies.append(veg.text)
originallist = sortedveggies.copy()

sortedveggies.sort()

print(sortedveggies)
assert sortedveggies == originallist