from django.shortcuts import render
from schnippjs.schnippforms import converter
from testproduct.models import News, Category
import json


def testing(request):
    '''
    Required for selenium tests; 
    '''    
    if len(News.objects.all()) == 0:
        raise Exception('''
            This view is used for Liveserver/selenium tests. Please create at least one News object if you want to 
            access this views manually.
        ''')
    fields = News._meta.get_all_field_names()
    fields.remove('id')
    return render(request, 'testing.html', {
        'schema': json.dumps(converter.form_for_model(News, fields, name='myform')),
        'context': json.dumps(converter.object_to_context(News.objects.all()[0]))
    })
