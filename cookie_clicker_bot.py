"""
cookie_clicker_bot.py
Author: Bryan Robbins
Github: Brobbins2001

The main entry point for the cookie clicker bot.

Defines init_driver and click_ticker functions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from save_load import load_save, save_save
import keyboard as kb, time
from interactions import buy_buildings, buy_upgrades, click_cookie, get_cookie, find_golden_cookie


def initialize_driver():
    """
    Initializes selenium webdriver and gets cookie clicker website.

    :return: selenium webdriver
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get('http://orteil.dashnet.org/cookieclicker/')
    return driver



def click_ticker():
    """
    The main clicking loop.

    Before entering the loop, initializes driver, and laods save if it exists.

    each iteration of the loop clicks the cookie,
    and attempts to buy buildings, upgrades, and save the file.
    """

    click_tick = 0
    driver = initialize_driver()
    cookie = get_cookie(driver)
    load_save(driver)
    while True:
        if not kb.is_pressed("`"):
            click_cookie(cookie)
            find_golden_cookie(driver)
            buy_upgrades(driver, click_tick)
            buy_buildings(driver, click_tick)
            save_save(driver, click_tick)
            click_tick += 1


click_ticker()
