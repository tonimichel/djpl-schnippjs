from django.db import models



def field_descriptor(name, field, default, **kwargs):
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
    if default:
        descriptor['default_value'] = default
    elif field.initial:
        descriptor['default_value'] = field.initial
    
    if field.required:
        descriptor['required'] = True
        
    descriptor.update(**kwargs)
    return descriptor

    



def text(name, field, default=None):
    '''
    Returns text field reprsentation or a dropdownselect in case  choices are 
    defined.
    '''
    return field_descriptor(name, field, default, type='text')
        

def textarea(name, field, default=None):
    return field_descriptor(name, field, default, type='textarea')
    
def integer(name, field, default=None):
    return field_descriptor(name, field, default, type='integer')
    
def floatingpoint(name, field, default=None):
    return field_descriptor(name, field, default, type='floatingpoint')
    
def modelchoice(name, field, default=None):
    fk_options = [dict(label=str(obj), value=obj.id) for obj in field.queryset]
    return field_descriptor(
        name, 
        field, 
        default,
        type='dropdownselect', 
        options=fk_options
    )

def dropdownselect(name, field, default=None):
    options = [dict(label=obj[1], value=obj[0]) for obj in field.choices]
    return field_descriptor(
        name, 
        field, 
        default,
        type='dropdownselect', 
        options=options
    )

def datepicker(name, field, default=None):
    return field_descriptor(name, field, default, type='datepicker')
    
def hiddeninput(name, field, default=None):
    
    print field._choices    
    
    return field_descriptor(name, field, default, type='hiddeninput')
    
    
    
    
