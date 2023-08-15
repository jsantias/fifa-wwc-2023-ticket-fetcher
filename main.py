from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from src.slack_client import send_notification
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
url = os.getenv("TARGET_URL")
hook_url = os.getenv("HOOK_URL")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#ignore
browser_session_url = driver.command_executor._url
session_id = driver.session_id    

print(browser_session_url)
print(session_id)

driver.get(url)

time.sleep(30)

driver.find_element("id", 'signInName').send_keys(username)
driver.find_element("id", 'password').send_keys(password)
driver.find_element("id", 'next').click()

time.sleep(15)
driver.find_element("id", "onetrust-accept-btn-handler").click()

while(True):
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, ("//*[contains(text(),'Adult')]")).click()
        driver.find_element(By.XPATH, ("//*[contains(text(),'Add to cart')]")).click()
        print("=================  HIT! =================")
        send_notification(hook_url=hook_url, message="Adult tickets found! Check me")
        break
    except Exception as e:
        print("Doesn't exist. Trying again")
        driver.refresh()