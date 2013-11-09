from schnippjs.schnippforms.mapping import FIELDS
from django.db import models
import datetime


def prepare(FIELDS):
    TUPLE_FIELDS = dict()
    for dj_field, schn_field in FIELDS.items():
        if type(dj_field) == tuple:
            TUPLE_FIELDS[dj_field] = schn_field
        else:
            TUPLE_FIELDS[(dj_field, dj_field.widget)] = schn_field
            
    return TUPLE_FIELDS


PREPARED_FIELDS = prepare(FIELDS)

def get_fields(form, context=None):
    context = context or {}
    schnields = []

    if not hasattr(form, 'fields'):
        raise FormInstancesOnly()    
    
    for name, field in form.fields.items():
        field_type = type(field)
        widget_type = type(field.widget)
        repr = PREPARED_FIELDS[(field_type, widget_type)]
        default_value = context.get(name, None)
        schnields.append(repr(name, field, default_value))
    return schnields    
    
def get_schema(form, name, context=None):
    return dict(
        name=name,
        fields=get_fields(form, context)
    )

def get_context(obj, fields=None):
    '''
    Converts ``obj`` to schnippform context.
    '''
    fields = fields or obj.__class__._meta.get_all_field_names() 
    context = {}
    for name in fields:
        val = getattr(obj, name)
        if type(obj.__class__._meta.get_field_by_name(name)[0]) in [models.ForeignKey]:
            # special handling for ForeignKey fields
            val = getattr(val, 'pk')
        
        if type(val) == datetime.date:
            val = val.strftime('%d.%m.%Y')
        
        if type(val) == datetime.datetime:
            val = 'not implemented yet'
            
        context[name] = val
    return context        
    

def get_field_from_schema(field_name, schema):
    '''
    Returns the field with name ``field_name`` from schema.
    '''
    for f in schema['fields']:
        if f['name'] == field_name:
            return f


class FormInstancesOnly(Exception):

    def __unicode__(self):
        return 'You probably passed a form class instead of an instance.'



