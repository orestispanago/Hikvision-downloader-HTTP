from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import json
import os

options = Options()
options.headless = False
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", os.getcwd() + "/raw")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")

browser = webdriver.Firefox(options=options)
url = 'http://150.140.194.27'
browser.get(url)

username = browser.find_element(By.ID, value="username")
password = browser.find_element(By.ID, value="password")

username.send_keys("YourUsername")
password.send_keys("YourPassword")

browser.find_element(By.XPATH, "//button[contains(.,'Login')]").click()
time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]").click()
time.sleep(3)

browser.find_element(By.XPATH, '//*[@title="Capture"]').click()

time.sleep(2)

url = 'view-source:http://150.140.194.27/ISAPI/Thermal/channels/2/thermometry/1/rulesTemperatureInfo?format=json'
browser.get(url)
content = browser.find_element(By.TAG_NAME, 'pre').text
parsed_json = json.loads(content)

max_temp = parsed_json.get('ThermometryRulesTemperatureInfoList') \
    .get('ThermometryRulesTemperatureInfo')[0] \
    .get("maxTemperature")

min_temp = parsed_json.get('ThermometryRulesTemperatureInfoList') \
    .get('ThermometryRulesTemperatureInfo')[0] \
    .get("minTemperature")
print(min_temp, max_temp)
browser.quit()
