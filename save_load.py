from interactions import click_until_successful
from selenium.webdriver.common.by import By
from os.path import exists
from settings import save_file_path

def click_options(driver):
    """
        Finds and clicks options button.
        :param driver: selenium driver
    """
    click_until_successful(driver, By.ID, "prefsButton")

def get_save_content(driver):
    """
        Gets save text element and text from save content element
        :param driver: selenium driver
        :return: string: save information
        """
    save_text_element = driver.find_element(By.XPATH,
                                            '//*[@id="textareaPrompt"]')
    return save_text_element.get_attribute('value')

def click_export(driver):
    """
        finds and clicks save export button.
        click_options must necessarily be called before this.
        :param driver: selenium webdriver.
        """
    click_until_successful(driver, By.XPATH,
                           '//*[@id="menu"]/div[3]/div[3]/a[1]')

def exit_export(driver):
    """
        finds and clicks the button to exit the export screen
        click_export must necessarily be called before this.
        :param driver: selenium driver
        """
    click_until_successful(driver, By.XPATH, '//*[@id="prompt"]/div[2]')

def click_import(driver):
    """
        finds and clicks the button to import saves
        click_options must necessarily be called before this.
        :param driver: selenium driver
        """
    click_until_successful(driver, By.XPATH,
                           '//*[@id="menu"]/div[3]/div[3]/a[2]')

def click_import_text_field(driver):
    """
        Clicks the import save text field.
        click_import must necessarily be called before this.
        :param driver: selenium driver
        """
    click_until_successful(driver, By.XPATH, '//*[@id="textareaPrompt"]')

def load_save_content():
    """
        Loads save content from "cookiesave.txt" file in %APPDATA%
        :return: string: save file contents
        """
    with open(save_file_path, 'r') as f:
        return f.read()

def type_save_content(driver):
    """
        Types the save content into import save text area
        click_import_text_field must necessarily be called before this.
        :param driver: selenium driver
        """
    save_content = load_save_content()
    textarea = driver.find_element(By.XPATH, '//*[@id="textareaPrompt"]')
    textarea.send_keys(save_content)

def click_load_button(driver):
    """
        Clicks the load save button when importing save
        type_save_content must necessarily be called before this.
        :param driver: selenium driver
    """
    click_until_successful(driver, By.XPATH, '//*[@id="promptOption0"]')



def load_save(driver):
    """
        Loads save from "cookiesave.txt" in %appdata%
        :param driver: selenium webdriver
        """
    if exists(save_file_path):
        click_options(driver)
        click_import(driver)
        click_import_text_field(driver)
        type_save_content(driver)
        click_load_button(driver)
        click_options(driver)

def save_save(driver, click_tick):
    """
        Saves save content to "cookiesave.txt" in %appdata%
        :param driver: selenium driver
        :param click_tick: current iteration of main loop
        """
    if click_tick % 1000 == 0:
        print("saving")
        click_options(driver)
        click_export(driver)
        save_content = get_save_content(driver)
        with open(save_file_path, 'w+') as f:
            f.write(save_content)
        exit_export(driver)
        click_options(driver)