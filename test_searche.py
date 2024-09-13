from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

#загружаем произвольные данные для регистрации из файлов json
with open('user.json',"r",encoding="utf-8") as f:
    user=json.loads(f.read())

with open('order.json',"r",encoding="utf-8") as f:
    order=json.loads(f.read())

driver = webdriver.Chrome()

# ОБОРАЧИВАЕМ все наши манипуляции в блок try, при возникновении ошибки на консоле будет исключение
try: 
    driver.get("https://www.saucedemo.com")
    time.sleep(1)

#Вводим имя в поле логин
    login=driver.find_element(By.NAME,"user-name")
    login.clear()
    login.send_keys(user["login"])
    time.sleep(1)
#Вводим пароль в поле пароль
    password=driver.find_element(By.NAME,"password")
    password.clear()
    password.send_keys(user["password"])
    time.sleep(1)
#Нажимаем кнопку регшистрации
    button=driver.find_element(By.NAME,"login-button").click()
    time.sleep(1)
#Выбираем товар "Sauce Labs Backpack"
    button=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)
#Заходим в корзину
    button=driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)
#Убуждаемся в наличии товара в корзине
    driver.find_element(By.ID,"item_4_title_link")
    time.sleep(2)
#Жмем кнопку "checkout"
    button=driver.find_element(By.ID,"checkout").click()
    time.sleep(2)
#Убеждаемся в появлении формы оформления заказа
    driver.find_element(By.CLASS_NAME,"checkout_info")
    time.sleep(2)
#Заполняем поля из файла json
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
 #Оформляем покупку
    button=driver.find_element(By.NAME,"continue").click()
    time.sleep(2)
#Проверяем покупку
    driver.find_element(By.CLASS_NAME,"summary_info_label")
    time.sleep(2)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()






 
