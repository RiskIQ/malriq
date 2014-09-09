#!/usr/bin/env python

import re
from riskiq import api

from canari.maltego.entities import IPv4Address, DNSName, Domain, URL

from .entities import IncidentEntity

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

def fix_dom(rec):
    ''' Remove period suffix '''
    if rec.endswith('.'):
        return rec[:-1]
    else:
        return rec

def incident_children(inc):
    response = []
    if inc.get('ip') or inc.get('url') or inc.get('hostname'):
        if IP_REGEX.match(inc.get('ip', '')):   
            ipe = IPv4Address(inc['ip'])
            ipe.ip = inc['ip']
            response += [ipe]
        if inc.get('url') and not IP_REGEX.match(inc['url']):
            urle = URL(inc['url'])
            urle.url = inc['url']
            response += [urle]
        if inc.get('hostname'):
            hostname = fix_dom(inc['hostname'])
            hoste = Domain(hostname)
            hoste.fqdn = hostname
            response += [hoste]
        ie = IncidentEntity(inc.get('url') or inc.get('ip') 
            or inc.get('hostname'))
        ie.url = inc.get('url', '')
        ie.ip = inc.get('ip', '')
        ie.hostname = inc.get('hostname', '')
        ie.score = inc.get('score', -1)
        ie.rank = inc.get('rank', -1)
        ie.description = inc.get('description', '')
        ie.phishing = inc.get('phishing', False)
        ie.malware = inc.get('malware', False)
        ie.spam = inc.get('spam', False)
        response += [ie]
    return response
