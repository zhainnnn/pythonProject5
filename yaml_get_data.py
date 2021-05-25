import yaml
import pathlib
import os
from log import log_def_start


def get_config():
    log_def_start('get_config')
    directory = pathlib.Path().resolve()
    file_name = 'config.yaml'
    file_path = os.path.join(directory, file_name)
    f = open(file_path, 'r',encoding='gbk')
    config = yaml.load(stream=f, Loader=yaml.Loader)
    f.close()

    return config.get('options')


if __name__ == '__main__':

    get_config()
