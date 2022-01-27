"""
interactions.py

Defines various functions for interacting with the webpage.
"""

from selenium.webdriver.common.by import By
from selenium.common import exceptions


def get_cookie(driver):
    """
    Get the large cookie element
    :param driver:
    :return: selenium web element representing the cookie
    """
    return driver.find_element(By.XPATH, '//*[@id="bigCookie"]')


def click_cookie(cookie):
    """
    Click the cookie element.
    :param cookie: selenium webelement representing the cookie
    """
    cookie.click()

def enumerating_element_click(driver, by, identifier, index_to_replace, num_elements, valid_class, descending=False):
    """
    Attempts to click a list of elements with similar XPATHS, replaces
    enum_index in xpath with ascending or descending integers, either from or to
    num_elements.
    :param driver: Selenium Webdriver
    :param by: selenium By class object. (E.g. By.XPATH)
    :param identifer: String: Identifier used by selenium to identify the elements
    :param inex_to_replace: integer: index of identifier to replace
    :param num_elements:  integer: number of elements to attempt to find and
    click
    :param valid_class: string:  checks the class of element against this
    string before clicking
    :param descending: boolean: Weather or not to click elements in an
    ascending or descending fashion
    :return:
    """
    for element in range(num_elements):
        if descending:
            element = num_elements - 1 - element
        identifier_fix = identifier[:index_to_replace] + str(element) + identifier[index_to_replace+1:]
        try:
            clickable_element = driver.find_element(by, identifier_fix)
            while clickable_element.get_attribute('class') == valid_class:
                driver.execute_script("arguments[0].scrollIntoView();", clickable_element)
                clickable_element.click()
                print(f"Bought {identifier_fix}")
                clickable_element = driver.find_element(by, identifier_fix)
        except:
            break

def buy_buildings(driver, click_tick):
    """
        Attempts to buy buildings
        :param click_tick: Integer, current iteration of click_ticker
        :param driver: Selenium webdriver
    """
    if click_tick % 500 == 0:
        enumerating_element_click(driver, By.XPATH, '//*[@id="product0"]', 16, 18, "product unlocked enabled", True)

def buy_upgrades(driver, click_tick):
    """
        Attempts to buy upgrades
        :param click_tick: Integer, current iteration of click_ticker
        :param driver: selenium webdriver
        """
    if click_tick % 751 == 0:
        enumerating_element_click(driver, By.XPATH ,'//*[@id="upgrade0"]' , 16, 244, "crate upgrade enabled")

def find_golden_cookie(driver):
    """
    Finds and attempts to click the golden cookie element
    :param driver: selenium webdriver
    """
    golden_cookies = driver.find_elements(By.CLASS_NAME, "shimmer")
    if golden_cookies:
        try:
            golden_cookie = driver.find_element(By.CLASS_NAME, "shimmer")
            golden_cookie.click()
        except exceptions.ElementNotInteractableException:
            print("unable to interact with golden cookie")
        except exceptions.ElementClickInterceptedException:
            print("unable to click golden cookie")


def click_until_successful(driver, by, identifer):
    """
    Attempts to click an element until is successfully clicks with no errors
    :param driver: selenium webdriver
    :param by: selenium By class (E.g. By.XPATH)
    :param identifer: string: identifier used by selenium to identify the element
    """
    unclicked = True
    while unclicked:
        try:
            element = driver.find_element(by, identifer)
            driver.execute_script("arguments[0].scrollIntoView();",
                                  element)
            element.click()
            unclicked = False
        except:
            pass