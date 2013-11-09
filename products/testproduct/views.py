from django.shortcuts import render
from schnippjs import schnippforms
from testproduct.models import News, Category
import json
from django.forms.models import modelform_factory
from django.http import HttpResponse

def testing(request):
    '''
    Required for selenium tests; 
    '''    
    
    cat = Category(name='Coding')
    cat.save()
    n = News(name='Djangoproductline', teaser='productivity', rating=1, somefloat=62.8, category=cat)
    n.save()
    
    if len(News.objects.all()) == 0:
        raise Exception('''
            This view is used for Liveserver/selenium tests. Please create at least one News object if you want to 
            access this views manually.
        ''')
    

    MyForm = modelform_factory(News)
    
    if request.method == 'POST':
        data = json.loads(request.POST['ajax_data'])
        form = MyForm(data)
        if form.is_valid():
            obj = form.save()
            return HttpResponse(json.dumps(schnippforms.get_context(obj)))
    else:
        form = MyForm()
                    
    return render(request, 'testing.html', {
        'schema': json.dumps(schnippforms.get_schema(form, name='myform')),
        'context': json.dumps(schnippforms.get_context(News.objects.all()[0]))
    })
