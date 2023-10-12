import yaml

from utils.config import PATH

import os


class YamlUtil:

    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def read_yaml(self):
        path = os.path.join(PATH, f'case/{self.file_name}')
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    print(YamlUtil('tese_case.yml').read_yaml)
