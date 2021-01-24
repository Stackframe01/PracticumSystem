import os
from sys import platform

from dacite import Config
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from workshop_system.apps.prof_standart.min_trud.utils import FileUtil
from workshop_system.utls import get_error_dict

PROF_STANDART_CODE_PATH_PARAM: str = 'prof_standart_code'
PROF_STANDART_CODE_PATH_PARAM_MATCH: str = f'<str:{PROF_STANDART_CODE_PATH_PARAM}>'

PROF_STANDART_NAME_QUERY_PARAM: str = 'name'

PROF_STANDART_REQUEST_ERROR: dict = get_error_dict('professional standart retrieve internal error')
PROF_STANDART_NOT_FOUND_ERROR: dict = get_error_dict('professional standart with specified code was not found')


class DaciteConfig:
    config: Config = Config(check_types=False)


class WebDriverConfig:
    _file_util: FileUtil = FileUtil()

    _platform_to_dir: dict = {
        'linux': 'chromedriver_linux64',
        'darwin': 'chromedriver_mac64',
        'win32': 'chromedriver_win32.exe'
    }

    def chrome(self, download_dir: str) -> WebDriver:
        chromedriver_dir: str = os.path.join(self._file_util.resources_dir, 'chromedriver')

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        prefs = {'download.default_directory': download_dir}
        options.add_experimental_option('prefs', prefs)

        chromedriver_path = os.path.join(chromedriver_dir, self._platform_to_dir.get(platform))
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

        return driver
