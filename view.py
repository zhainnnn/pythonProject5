from yaml_get_data import get_config
import pathlib


def views():
    flags = get_config()
    print('当前配置为:')
    for key,value in flags.items():
        print(key+':'+str(value))
# for key,value in list.items():
#     print(key+':'+value)

#print(get_config())
e=['asd','qwe']
w=['oiujg','jh']
print(e+w)
directory = pathlib.Path().resolve()
print(directory)




