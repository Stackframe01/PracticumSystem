import glob
import os
import time

import workshop_system


class FileReadError(Exception):
    def __init__(self, code: int = None, message: str = None) -> None:
        super().__init__(self, f'File not found error, code: {code}, message: {message}')


class FileUtil:
    resources_dir: str = os.path.join(os.path.dirname(workshop_system.__file__), 'resources')
    downloads_dir: str = os.path.join(resources_dir, 'downloads')
    chromedriver_dir: str = os.path.join(resources_dir, 'chromedriver')

    @classmethod
    def _get_recent_file(cls, dir_path) -> str:
        files: [str] = glob.glob(f'{dir_path}{os.path.sep}*')

        if files:
            return max(files, key=os.path.getctime)
        else:
            raise FileReadError(1, f'directory: {dir_path}')

    @classmethod
    def _remove_dir(cls, dir_path) -> None:
        files: [str] = glob.glob(f'{dir_path}{os.path.sep}*')
        if files:
            for file in files:
                os.remove(file)
        os.rmdir(dir_path)

    @classmethod
    def get_download_dir_name(cls, file_name: str) -> str:
        file_name = file_name.lower().replace(' ', '_')
        return os.path.join(cls.downloads_dir, f'{file_name}_{time.time()}')

    @classmethod
    def read_recent_and_remove(cls, dir_path: str) -> str:
        recent_file: str = cls._get_recent_file(dir_path)

        try:
            with open(recent_file) as file:
                data: str = file.read()
        except FileNotFoundError:
            raise FileReadError(1, f'path: {recent_file}')

        cls._remove_dir(dir_path)

        return data
