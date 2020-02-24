import os
import time
import glob
from sys import platform
from selenium import webdriver


def initialize_chromedriver():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'chromedriver'))
    driver = webdriver

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Turn off browser display
    options.add_experimental_option('prefs', {'download.default_directory': os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_data', 'professional_standards')) + os.sep})

    if platform == 'linux' or platform == 'linux2':
        driver = webdriver.Chrome(os.path.join(root, 'chromedriver_linux64'), options=options)
    elif platform == 'darwin':
        driver = webdriver.Chrome(os.path.join(root, 'chromedriver_mac64'), options=options)
    elif platform == 'win32':
        driver = webdriver.Chrome(os.path.join(root, 'chromedriver_win32.exe'), options=options)

    return driver


def download_professional_standards_by_name(name):
    driver = initialize_chromedriver()
    driver.get('https://profstandart.rosmintrud.ru/obshchiy-informatsionnyy-blok/' +
               'natsionalnyy-reestr-professionalnykh-standartov/reestr-professionalnykh-standartov/')

    show_button = driver.find_element_by_class_name('add')
    if show_button.text == 'Поиск »':
        show_button.click()
    driver.find_element_by_name('arrFilter_ff[NAME]').send_keys(name)
    driver.find_element_by_name('set_filter').click()
    time.sleep(10)
    driver.find_element_by_xpath('//input[@type="submit" and @value="Скачать в XML"]').click()

    time.sleep(1)
    driver.quit()


def download_professional_standards_by_id(professional_standard_id):
    driver = initialize_chromedriver()
    driver.get('https://profstandart.rosmintrud.ru/obshchiy-informatsionnyy-blok/natsionalnyy-reestr-professionalnykh'
               '-standartov/reestr-professionalnykh-standartov/')

    driver.execute_script('downloadXml(\'{}\')'.format(professional_standard_id))
    time.sleep(1)
    driver.quit()


def get_latest_downloaded_professional_standards():
    with open(max(glob.glob(os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_data', 'professional_standards', '*.xml'))),
            key=os.path.getctime)) as f:
        return f.read()


def clear_downloads():
    for f in glob.glob(os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_data', 'professional_standards', '*.xml'))):
        os.remove(f)


if __name__ == '__main__':
    pass
