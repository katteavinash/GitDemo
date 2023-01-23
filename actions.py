import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("Headless")
chrome_option.add_argument("")

service_obj = Service("Users/Avinash Katte/Downloads/chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_option)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.double_click(driver.find_element(By.LINK_TEXT, "Reload")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
driver.get_screenshot_as_file("screen.png")
time.sleep(5)