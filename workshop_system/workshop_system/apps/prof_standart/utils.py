import glob
import os


class FileUtil:
    resources_dir: str
    downloads_dir: str
    chromedriver_dir: str

    def __init__(self, resources_dir: str):
        self.resources_dir = resources_dir
        self.downloads_dir = os.path.join(self.resources_dir, 'downloads')
        self.chromedriver_dir = os.path.join(self.resources_dir, 'chromedriver')

    def clear_downloads(self):
        for f in glob.glob(self.downloads_dir):
            os.remove(f)

    def _get_latest_download_path(self):
        return max(glob.glob(os.path.abspath(self.downloads_dir)), key=os.path.getctime)

    def read_latest_download(self):
        latest_path = self._get_latest_download_path()
        with open(latest_path) as file:
            return file.read()
