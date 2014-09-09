#!/usr/bin/env python

import re
from riskiq import api

__author__ = 'Johan Nestaas'
__copyright__ = 'Copyright 2014, Malriq Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'Johan Nestaas'
__email__ = 'johan@riskiq.net'
__status__ = 'Development'

__all__ = [
    'entities'
]

IP_REGEX = re.compile(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.([0-9]{1,3}|\*|[0-9]{1,3}/[0-9]{1,2})$')

def get_client(config):
    try:
        token = config['riskiq_api_credentials/token']
        secret = config['riskiq_api_credentials/private_key']
    except:
        raise ValueError('Please input RiskIQ API creds in ~/.canari/malriq.conf')
    if not (token and secret):
        raise ValueError('Please input RiskIQ API creds in ~/.canari/malriq.conf')
    return api.Client(token, secret)
