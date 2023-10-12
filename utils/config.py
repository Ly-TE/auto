import os

PATH = os.path.dirname(os.path.dirname(__file__))
ENV = {
    'release': {
        'host': 'https://geoip.leigod.com'

    },
    'dev': {

    },
    'vf': {

    }

}

env_name = 'release'
host = ENV[env_name]['host']
