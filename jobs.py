from get_cmd import over_cmd,config_cmd
from yaml_get_data import get_config
from view import views
import os


def jobs():
    os.system(over_cmd(config_cmd(get_config())))

views()
input('是否开始')
jobs()