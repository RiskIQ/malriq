#!/usr/bin/env python
import os

from canari.maltego.entities import IPv4Address, DNSName, Domain, URL
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import PDNSEntity

from riskiq import api

__author__ = 'Johan Nestaas'
__copyright__ = 'Copyright 2014, Malriq Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
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
TODO: set the appropriate configuration parameters for your transform.
"""
@configure(
    label='To RiskIQ PDNSEntity [RiskIQ Passive DNS]',
    description='Returns passive DNS entries from RiskIQ',
    uuids=['malriq.v2.MalriqEntityToPDNS'],
    inputs=[
        ('Malriq', Domain), ('Malriq', IPv4Address),
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

    # Report transform progress
    prog = 10
    progress(prog)
    # Send a debugging message to the Maltego UI console
    debug('Starting RiskIQ incident lookup...')
    debug('entities:')
    debug(str(request.entities))
    debug('vars:')
    debug(str(vars(request.entities[0])))
    url = request.entities[0].value
    config = {}
    execfile(os.path.join(os.getenv('HOME'), '.creds.py'), config)
    creds = config['api_creds']['testing']
    debug(str(vars(request.entities[0])))
    url = request.entities[0].value
    config = {}
    execfile(os.path.join(os.getenv('HOME'), '.creds.py'), config)
    creds = config['api_creds']['testing']
    client = api.Client(creds['token'], creds['private_key'])
    api_response = client.
    incidents = [x['resource'] for x in api_response['incident']]
    prog += 10
    progress(prog)
    total = 80 - prog
    if not incidents:
        progress(100)
        return response
    prog_inc = total / len(incidents)
    for inc in incidents:
        ie = IncidentEntity(inc['ip'])
        ie.url = inc['url']
        ie.ip = inc['ip']
        ie.score = inc['score']
        ie.rank = inc['rank']
        ie.phishing = inc['phishing']
        ie.malware = inc['malware']
        ie.spam = inc['spam']
        response += ie
        ue = URL(inc['ip'])
        ue.url = inc['url']
        response += ue
        prog += prog_inc
        progress(prog)
    progress(100)
    """
    debug(str(config))
    debug(str(vars(config)))
    return response


"""
Called if transform interrupted. It's presence is optional; you can remove this function if you don't need to do any
resource clean up.

TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable 
"""
def onterminate():
    debug('Caught signal... exiting.')
    exit(0)