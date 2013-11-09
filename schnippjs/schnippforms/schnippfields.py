from django.db import models



def field_descriptor(name, field, **kwargs):
    '''
    Generates the basic schnipp field descriptor.
    Use kwargs to set field-individual attributes.
    '''
    descriptor = {
        'name': name,
        'label': field.label or name,
    }    
    

    if field.help_text:
        descriptor['description'] = field.help_text
    if field.initial:
        descriptor['default_value'] = field.initial
    if field.required:
        descriptor['required'] = True
        
    descriptor.update(**kwargs)
    return descriptor





def text(name, field, instance=None):
    '''
    Returns text field reprsentation or a dropdownselect in case  choices are 
    defined.
    '''
    return field_descriptor(name, field, type='text')
    if field.choices != []:
        options = [dict(label=obj[1], value=obj[0]) for obj in field.choices]
        return field_descriptor(field, 
            type='dropdownselect', 
            options=options
        )
    else:pass
        

def textarea(name, field, instance=None):
    return field_descriptor(name, field, type='textarea')
    
def integer(name, field, instance=None):
    return field_descriptor(name, field, type='integer')
    
def floatingpoint(name, field, instance=None):
    return field_descriptor(name, field, type='floatingpoint')
    
def modelchoice(name, field, instance=None):
    fk_options = [dict(label=str(obj), value=obj.id) for obj in field.queryset]
    return field_descriptor(
        name, 
        field, 
        type='dropdownselect', 
        options=fk_options
    )

def dropdownselect(name, field, instance=None):
    options = [dict(label=obj[1], value=obj[0]) for obj in field.choices]
    return field_descriptor(
        name, 
        field, 
        type='dropdownselect', 
        options=options
    )

def datepicker(name, field, instance=None):
    return field_descriptor(name, field, type='datepicker')
    
    
    
    
