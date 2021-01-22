import xmltodict
from selenium.webdriver.remote.webdriver import WebDriver

from workshop_system.apps.prof_standart.utils import FileUtil


class ProfstandartClient:
    _file_util: FileUtil
    _webdriver: WebDriver
    _base_url = 'profstandart.rosmintrud.ru'
    _profstandart_registry = 'obshchiy-informatsionnyy-blok/natsionalnyy-reestr-' \
                             'professionalnykh-standartov/reestr-professionalnykh-standartov'
    _download_dir: str

    def __init__(self, file_util: FileUtil, webdriver: WebDriver):
        self._file_util = file_util
        self._webdriver = webdriver

    def _download_profstandart_by_code(self, code: str) -> None:
        self._webdriver.get(f'https://{self._base_url}/{self._profstandart_registry}/')
        show_button = self._webdriver.find_element_by_class_name('ps-hide-show')

        if show_button.text == 'Развернуть':
            show_button.click()

        profstandart_name_input = self._webdriver.find_element_by_name('arrFilter_ff[CODE]')
        self._webdriver.implicitly_wait(10)
        profstandart_name_input.send_keys(code)

        filter_buttons = self._webdriver.find_element_by_name('set_filter')
        filter_buttons.click()

        download_buttons = self._webdriver.find_elements_by_name('save')
        for download_button in download_buttons:
            value = download_button.get_property('value')
            if value == 'Скачать в XML':
                download_button.click()
                break

        self._webdriver.quit()

    def get_profstandart_by_code(self, code: str) -> str:
        self._download_profstandart_by_code(code=code)
        profstandart = self._file_util.read_latest_download()
        profstandart_dict = xmltodict.parse(profstandart)
        return profstandart_dict
