"""
interactions.py

Defines various functions for interacting with the webpage.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


def xpath_enumerating_click(driver, xpath, enum_index, num_elements,
                            valid_class, descending=False):
    """
    Attempts to click a list of elements with similar XPATHS, replaces
    enum_index in xpath with ascending or descending integers, either from or to
    num_elements.

    :param driver: Selenium Webdriver
    :param xpath: String: XPATH
    :param enum_index: integer: index of XPATH to replace
    :param num_elements:  integer: number of elements to attempt to find and
    click

    :param valid_class: string:  checks the class of element against this
    string before clicking

    :param descending: boolean: Weather or not to click elements in an
    ascending or descending fashion
    :return:
    """
    for x in range(num_elements):
        if descending:
            x = num_elements-1-x
        new_xpath = xpath[:enum_index] + str(x) + xpath[enum_index+1:]
        try:
            item = driver.find_element(By.XPATH, new_xpath)
            if item.get_attribute("class") == valid_class:
                item.click()
        except:
            break


def buy_upgrades(click_tick, driver):
    """
    Attempts to buy upgrades
    :param click_tick: Integer, current iteration of click_ticker
    :param driver: selenium webdriver
    """
    if click_tick % 753 == 0:
        xpath_enumerating_click(driver, '//*[@id="upgrade0"]', 16, 244,
                               "crate upgrade enabled")


def buy_buildings(click_tick, driver):
    """
    Attempts to buy buildings
    :param click_tick: Integer, current iteration of click_ticker
    :param driver: Selenium webdriver
    """
    try:
        if click_tick % 500 == 0:
            xpath_enumerating_click(driver, '//*[@id="product0"]', 16, 18,
                                   "product unlocked enabled", True)
    except ElementClickInterceptedException as e:
        print(e)
        golden_cookie = driver.find_element(By.CLASS_NAME, "shimmer")
        golden_cookie.click()


def click_until_successful(driver, by_what, identifier):
    """
    Attempt to find and click an element until the click is successful.
    :param driver: Selenium webdriver
    :param by_what: Selenium "By" object provided to driver.find_element()
     (E.g. "By.XPATH"
    :param identifier: identifier given to driver.find_element
    """
    unclicked = True
    while unclicked:
        try:
            button = driver.find_element(by_what, identifier)
            button.click()
            unclicked = False
        except:
            pass
