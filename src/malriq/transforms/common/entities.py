#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'Johan Nestaas'
__copyright__ = 'Copyright 2014, Malriq Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Johan Nestaas'
__email__ = 'johan@riskiq.net'
__status__ = 'Development'

__all__ = [
    'MalriqEntity',
    'IncidentEntity',
    'PDNSEntity',
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyMalriqEntity will
have an entity type name of malriq.MyMalriqEntity. When adding a new entity in Maltego, you will have to specify this
name (malriq.MyMalriqEntity) in the 'Unique entity type' field.
"""
class MalriqEntity(Entity):
    _namespace_ = 'malriq'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
    - is_value: a boolean value that determines whether the field is also the default value of the entity object.
TODO: define as many custom fields and entity types as you wish:)
"""    

@EntityField(name='malriq.url', propname='url', displayname='URL')
@EntityField(name='malriq.ip', propname='ip', displayname='IPv4')
@EntityField(name='malriq.score', propname='score', displayname='Score', type=EntityFieldType.Integer)
@EntityField(name='malriq.rank', propname='rank', displayname='Rank', type=EntityFieldType.Integer)
@EntityField(name='malriq.phishing', propname='phishing', displayname='Phishing', type=EntityFieldType.Bool)
@EntityField(name='malriq.malware', propname='malware', displayname='Malware', type=EntityFieldType.Bool)
@EntityField(name='malriq.spam', propname='spam', displayname='Spam', type=EntityFieldType.Bool)
class IncidentEntity(MalriqEntity):
    """
    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
    'my.fancy.EntityType'
    """
    # _name_ = 'my.fancy.EntityType'
    pass

@EntityField(name='malriq.ip', propname='ip', displayname='IPv4')
class PDNSEntity(MalriqEntity):
    """
    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
    'my.fancy.EntityType'
    """
    # _name_ = 'my.fancy.EntityType'
    pass
