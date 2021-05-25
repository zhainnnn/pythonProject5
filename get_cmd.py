import os
from yaml_get_data import get_config


def config_cmd(config):
    flags=dict(
        k=config['size'],
        n=config['number_of_plots'],
        b=config['memory_buffer'],
        f=config['farmer_pk'],
        p=config['pool_pk'],
        a=config['fingerprint'],
        t=config['tmp_dir'],
        d=config['final_dir'],
        r=config['number_of_threads'],
        u=config['number_of_buckets'],
        e=config['bitfield_plotting']
    )
    #print(flags)
    if config['tmp_dir_2']:
        flags['2']=config['tmp_dir_2']
    data = ['chia plots create']
    for key, value in flags.items():
        flag = f'-{key}'
        if value == None:# or value==True:
            continue
        if key=='e':
            if value==True:
                data.append(flag)
            continue
        data.append(flag)
        data.append(str(value))
    return data


def over_cmd(list):
    path=os.path.abspath('chia')
    job=' '.join(list)
    overcmd='cd '+path+' && '+job
    return overcmd





