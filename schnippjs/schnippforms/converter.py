from .mapping import MAPPING
from .import schnippfields
from django.db import models

def fields_for_model(model, fields):
    '''
    Generates the schnippform fields reprsentation of ``model`` by taking the specified 
    ``fields`` into account.
    '''
    schnipp_repr = []
    for field_name in fields:
        field = model._meta.get_field_by_name(field_name)[0]
        try:
            translator = MAPPING[type(field)]
        except KeyError:
            raise SchnippRepresentationDoesNotExist('There is no representation for this model field: %s' % type(field))
        schnipp_repr.append(translator(field))
    return schnipp_repr

    
def form_for_model(model, fields, name):
    '''
    Returns the schnippform form representation of ``model`` by taking ``fields`` into account.
    '''
    return {
        'name': name,
        'fields': fields_for_model(model, fields)
    }
    

def object_to_context(obj, fields):
    '''
    Converts ``obj`` to schnippform context.
    '''
    schema = dict()
    for name in fields:
        val = getattr(obj, name)
        if type(obj.__class__._meta.get_field_by_name(name)[0]) in [models.ForeignKey]:
            # special handling for ForeignKey fields
            val = getattr(val, 'pk')
        schema[name] = val
    return schema



class SchnippRepresentationDoesNotExist(Exception):
    pass
