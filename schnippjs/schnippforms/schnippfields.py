from django.db import models



def field_descriptor(field, **kwargs):
    '''
    Generates the basic schnipp field descriptor.
    Use kwargs to set field-individual attributes.
    '''
    descriptor = {
        'name': field.name,
        'label': field.verbose_name or field_name,
    }    
    
    if field.help_text:
        descriptor['description'] = field.help_text
    if field.default != models.fields.NOT_PROVIDED:
        descriptor['default_value'] = field.default

    if not (field.null or field.blank):
        descriptor['required'] = True
        
    descriptor.update(**kwargs)
    return descriptor





def text(field):
    '''
    Returns text field reprsentation or a dropdownselect in case  choices are 
    defined.
    '''
    if field.choices != None:
        options = [dict(label=obj[1], value=obj[0]) for obj in field.choices]
        return field_descriptor(field, 
            type='dropdownselect', 
            options=options
        )
    else:
        return field_descriptor(field, type='text')

def textarea(field):
    return field_descriptor(field, type='textarea')
    
def integer(field):
    return field_descriptor(field, type='integer')
    
def floatingpoint(field):
    return field_descriptor(field, type='floatingpoint')
    
def foreignkey(field):
    fk_options = [dict(label=str(obj), value=obj.id) for obj in field.rel.to.objects.all()]
    return field_descriptor(field, 
        type='dropdownselect', 
        options=fk_options
    )
