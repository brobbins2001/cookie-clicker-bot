from selenium import webdriver
from selenium.webdriver.common.by import By


def init_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get('http://orteil.dashnet.org/cookieclicker/')
    cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    return driver, cookie


def href_enumerating_click(driver, href,enum_index,num_elements, valid_class,
                           descending=False):
    for x in range(num_elements):
        if descending:
            x = num_elements-1-x
        new_href = href[:enum_index] + str(x) + href[enum_index+1:]
        try:
            item = driver.find_element(By.XPATH, new_href)
            if item.get_attribute("class") == valid_class:
                item.click()
        except:
            break;


def buy_upgrades(click_tick, driver):
    if click_tick % 75 == 0:
        href_enumerating_click(driver, '//*[@id="upgrade0"]', 16, 244,
                               "crate upgrade enabled")


def buy_buildings(click_tick, driver):
    if click_tick % 50 == 0:
        href_enumerating_click(driver, '//*[@id="product0"]', 16, 18,
                               "product unlocked enabled", True)


def click_ticker():
    click_tick = 0
    driver, cookie = init_driver()
    try:
        while True:
            click_tick += 1
            cookie.click()
            buy_upgrades(click_tick, driver)
            buy_buildings(click_tick, driver)
    except KeyboardInterrupt:
        input("You can press enter to close the game, "
              "or save your game file then press enter.")
        exit()


click_ticker()
