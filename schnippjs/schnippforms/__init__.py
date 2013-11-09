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

def get_fields(form, instance=None):
    schnields = []
    for name, field in form.fields.items():
        field_type = type(field)
        widget_type = type(field.widget)
        repr = PREPARED_FIELDS[(field_type, widget_type)]
        schnields.append(repr(name, field, instance))
    return schnields    
    
    
    
def get_schema(form, name, instance=None):
    return dict(
        name=name,
        fields=get_fields(form, instance)
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
            val = 'HURENSOHN'
            
            
        context[name] = val
    return context        
    


