import os
from sys import platform

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from workshop_system.apps.prof_standart.utils import FileUtil


class WebDriverConfig:
    _file_util: FileUtil
    _platform_to_dir = {
        'linux': 'chromedriver_linux64',
        'darwin': 'chromedriver_mac64',
        'win32': 'chromedriver_win32.exe'
    }

    def __init__(self, file_util: FileUtil) -> None:
        self._file_util = file_util

    def chrome(self) -> WebDriver:
        chromedriver_dir = os.path.join(self._file_util.resources_dir, 'chromedriver')

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        prefs = {'download.default_directory': self._file_util.downloads_dir}
        options.add_experimental_option('prefs', prefs)

        chromedriver_path = os.path.join(chromedriver_dir, self._platform_to_dir.get(platform))
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        return driver
