import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("Users/Avinash Katte/Downloads/chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
#driver.back()
time.sleep(5)
driver.find_element(By.ID, 'autocomplete').send_keys('ind')
time.sleep(5)
countries = driver.find_elements(By.CLASS_NAME, 'ui-menu-item-wrapper')

for country in countries:
    if country.text == 'India':
        country.click()
        break
assert driver.find_element(By.ID, 'autocomplete').get_attribute('value') == "India"
checkbox = driver.find_elements(By.XPATH, "//*[@type='checkbox']")
print(len(checkbox))
for cb in checkbox:
    if cb.get_attribute("value") == "option1":
        cb.click()
        assert cb.is_selected()
        break
time.sleep(5)
#//input[@type='radio']
radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
radio[1].click()
abc = radio[1].is_selected()
print(abc)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id ='name']").send_keys('Avinash')
driver.find_element(By.XPATH, "//input[@id ='alertbtn']").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
name = "Avinash"
assert name in alerttext
time.sleep(5)