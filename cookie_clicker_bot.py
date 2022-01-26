"""
cookie_clicker_bot.py
Author: Bryan Robbins
Github: Brobbins2001

The main entry point for the cookie clicker bot.

Defines init_driver and click_ticker functions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from save_load import load_save, save_file
from interactions import buy_buildings, buy_upgrades


def init_driver():
    """

    :return: driver: A selenium webDriver Instance
             cookie: the cookie web element
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get('http://orteil.dashnet.org/cookieclicker/')
    cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    return driver, cookie


def click_ticker():
    """
    The main clicking loop.

    Before entering the loop, initializes driver, and laods save if it exists.

    each iteration of the loop clicks the cookie,
    and attempts to buy buildings, upgrades, and save the file.
    """
    click_tick = 0
    driver, cookie = init_driver()
    load_save(driver)
    while True:
        click_tick += 1
        cookie.click()
        buy_upgrades(click_tick, driver)
        buy_buildings(click_tick, driver)
        save_file(driver, click_tick)


click_ticker()
