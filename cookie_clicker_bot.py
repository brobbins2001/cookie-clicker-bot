from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("C:/Users/mason/Documents/chromedriver.exe", options=options)
driver.get('http://orteil.dashnet.org/cookieclicker/')
a = ActionChains(driver)

cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
store = driver.find_element(By.XPATH, '//*[@id="products"]')
x = 0
'//*[@id="products"]'

def hover_over(element):
    try:
        a.move_to_element(element).perform()
    except Exception as e:
        pass



while True:
    x += 1
    cookie.click()

    if x % 750 == 0:
        print("TRYING TO BUY")
        try:
            for y in range(234):
                item_list = driver.find_elements(By.XPATH, f'//*[@id="upgrade{y}"]')
                item = driver.find_element(By.XPATH, f'//*[@id="upgrade{y}"]')
                isPresent = len(item_list) > 0
                if isPresent:
                    if item.get_attribute("class") == "crate upgrade enabled":
                        #hover_over(item)

                            item.click()
        except:
            pass

    if x % 500 == 0:
        print(x/500)
        for y in range(18):
            item_list = driver.find_elements(By.XPATH, f'//*[@id="product{y}"]')
            item = driver.find_element(By.XPATH, f'//*[@id="product{y}"]')
            isPresent = len(item_list) > 0
            if isPresent:
                if item.get_attribute("class") == "product unlocked enabled":
                    #hover_over(item)
                    try:
                        for z in range(20):
                            item.click()
                    except:
                        pass

