#!/usr/bin/env python
import os

from canari.maltego.entities import IPv4Address, DNSName, Domain, URL
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common import IP_REGEX, get_client
from common.entities import IncidentEntity

__author__ = 'Johan Nestaas'
__copyright__ = 'Copyright 2014, Malriq Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'Johan Nestaas'
__email__ = 'johan@riskiq.net'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]

# Uncomment the line below if the transform needs to run as super-user
#@superuser
"""
The @configure decorator tells mtginstall how to install the transform in Maltego. It takes the following parameters:
    - label:        the name of the transform as it appears in the Maltego UI transform selection menu
    - description:  a short description of the transform
    - uuids:        a list of unique transform IDs, one per input type. The order of this list must match that of the 
                    inputs parameter. Make sure you account for entity type inheritance in Maltego. For example, if you
                    choose a DNSName entity type as your input type you do not need to specify it again for MXRecord, 
                    NSRecord, etc.
    - inputs:       a list of tuples where the first item is the name of the transform set the transform should be part
                    of, and the second item is the input entity type.
    - debug:        Whether or not the debugging window should appear in Maltego's UI when running the transform.
    - remote:       Whether or not the transform can be used as a remote transform in Plume.
ODO: set the appropriate configuration parameters for your transform.
"""
@configure(
    label='To RiskIQ Incidents [Incident, Domain, URL, IPv4]',
    description='Returns a list of incidents from RiskIQ',
    uuids=['malriq.v2.DomainToIncident', 'malriq.v2.URLToIncident',
           'malriq.v2.IPv4ToIncident'],
    inputs=[
        ('RiskIQ', Domain), ('RiskIQ', URL), ('RiskIQ', IPv4Address),
    ],
    remote=False,
    debug=True,
)
def dotransform(request, response, config):
    """
    The dotransform function is our transform's entry point. The request object has the following properties:
        - value:    a string containing the value of the input entity.
        - fields:   a dictionary of entity field names and their respective values of the input entity.
        - params:   any additional command-line arguments to be passed to the transform.
        - entity:   the information above is serialized into an Entity object. The entity type is determined
                    by the inputs field in @configure for local transforms. For remote transforms, the entity
                    type is determined by the information in the body of the request. Local transforms suffer
                    from one limitation: if more than one entity type is listed in the inputs field of @configure,
                    the entity type might not be resolvable. Therefore, this should not be referenced in local
                    transforms if there is more than one input entity type defined in @configure.

    The response object is a container for output entities, UI messages, and exception messages. The config object
    contains a key-value store of the configuration file.
    TODO: write your data mining logic below.
    """
    client = get_client(config)
    prog = 10
    progress(prog)
    debug('Starting RiskIQ incident lookup...')
    url = request.entities[0].value
    api_response = client.get_blacklist_incident(url)
    incidents = [x['resource'] for x in api_response['incident']]
    prog += 10
    progress(prog)
    total = 80 - prog
    if not incidents:
        progress(100)
        return response
    prog_inc = total / len(incidents)
    for inc in incidents:
        if inc.get('ip') or inc.get('url'):
            if IP_REGEX.match(inc.get('ip', '')):   
                ipe = IPv4Address(inc['ip'])
                ipe.ip = inc['ip']
                response += ipe
            if inc.get('url') and not IP_REGEX.match(inc['url']):
                urle = URL(inc['url'])
                urle.url = inc['url']
                response += urle
            ie = IncidentEntity(inc.get('ip') or inc.get('url'))
            ie.url = inc.get('url', '')
            ie.ip = inc.get('ip', '')
            ie.score = inc.get('score', -1)
            ie.rank = inc.get('rank', -1)
            ie.phishing = inc.get('phishing', False)
            ie.malware = inc.get('malware', False)
            ie.spam = inc.get('spam', False)
            response += ie
        prog += prog_inc
        progress(prog)
    progress(100)
    return response


"""
Called if transform interrupted. It's presence is optional; you can remove this function if you don't need to do any
resource clean up.

TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable 
"""
def onterminate():
    debug('Caught signal... exiting.')
    exit(0)
