from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import json

with open('user.json',"r",encoding="utf-8") as f:
    user=json.loads(f.read())

with open('order.json',"r",encoding="utf-8") as f:
    order=json.loads(f.read())

driver = webdriver.Chrome()

try: 
    driver.get("https://www.saucedemo.com")
    #behave -i  my_feature.feature --no-capturedriver.find_element(By.CLASS_NAME,"user-name")
    time.sleep(1)

    login=driver.find_element(By.NAME,"user-name")
    login.clear()
    login.send_keys(user["login"])
    time.sleep(1)

    password=driver.find_element(By.NAME,"password")
    password.clear()
    password.send_keys(user["password"])
    time.sleep(1)

    button=driver.find_element(By.NAME,"login-button").click()
    time.sleep(1)

    button=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    button=driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)

    driver.find_element(By.ID,"item_4_title_link")
    time.sleep(2)

    button=driver.find_element(By.ID,"checkout").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME,"checkout_info")
    time.sleep(2)

    password=driver.find_element(By.NAME,"firstName")
    password.clear()
    password.send_keys(order["firstName"])
    time.sleep(1)

    password=driver.find_element(By.NAME,"lastName")
    password.clear()
    password.send_keys(order["lastName"])
    time.sleep(1)

    password=driver.find_element(By.NAME,"postalCode")
    password.clear()
    password.send_keys(order["postal-Code"])
    time.sleep(1)
 
    button=driver.find_element(By.NAME,"continue").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME,"summary_info_label")
    time.sleep(2)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()






 
