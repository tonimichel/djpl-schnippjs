djpl-schnippjs
====================================

A django_productline feature integrating `schnipp-js <https://github.com/henzk/schnippjs/>`_.
Hooks the schnipp-js javascript framework into your ``media_includes.html`` and provides
a model to schnippform schema translation which generates a form schema from your django model.



Installation
====================================

1) ``pip install - e git+https://github.com/tonimichel/djpl-schnippjs.git#djpl-schnippjs.git``.



Generating schnippforms
==========================

Let's consider a simple example. Imagine your project consists of a News feature providing a ``News`` 
model. The frontend is fully javascript. As we need a programmtic form api and some MVC in our frontend code
we decide to use schnippjs. Instead of declaring the form schema manually we just can convert our models to a schnippform
schema and pass them to the template.

.. code-block:: python

    from django.shortcuts import render
    from schnippjs.schnippforms import converter
    from testproduct.models import News, Category
    import json


    def myview(request, id):
    
        n = News.objects.get(pk=id)
        form_schema = converter.form_for_model(n, fields=['name', 'category', 'teaser'], name='myform')
        form_context = converter.object_to_context(n)
    
        return render(request, 'testing.html', {
            'schema': json.dumps(form_schema),
            'context': json.dumps(form_context)
        })
        

.. code-block:: javascript

    $(function() {
        var form = schnipp.dynforms.form({{ schema|safe }}, {{ context|safe }});
        $('#b').append(form.render())
        form.initialize()
        
    })

        
Take a look at the testproduct in ``products/testproduct`` for a complete example.
        
        

