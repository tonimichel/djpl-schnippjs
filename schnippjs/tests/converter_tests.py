from django.test import TestCase
from django import db
from schnippjs.schnippforms import converter
from testproduct.models import Category, News

class FieldsForModelTests(TestCase):
    '''
    Test schnippform generation.
    '''


    def check_attrs(self, field, descriptor):
        '''
        Ensure that descriptor has the supposed fields.
        '''
        if hasattr(field, 'verbose_name') and field.verbose_name:
            self.assertEquals(descriptor['label'], field.verbose_name)
        else:
            self.assertEquals(descriptor['label'], field.name)
        if field.help_text:
            self.assertEquals(descriptor['description'], field.help_text)
        if field.default != db.models.fields.NOT_PROVIDED:
            self.assertEquals(descriptor['default_value'], field.default)
        if not (field.null or field.blank):
            self.assertTrue(descriptor['required'])


    def test_field_types(self):
        '''
        Iterate all fields of the test model and check that they
        exist in the MAPPING; check the resulting descriptor attrs.
        '''
        for name in News._meta.get_all_field_names():
            if name == 'id':
                break
            field = News._meta.get_field_by_name(name)[0]
            translator = converter.MAPPING[type(field)]
            descriptor = translator(field)
            self.check_attrs(field, descriptor)


    def test_fk(self):
        '''
        Test the the foreignkey translation.
        '''
        n = News(name='a', teaser='b', rating=1, somefloat=0.2)
        n.save()
        
        for i in range(0, 5):
            c = Category(name=i)
            c.save()

        field = News._meta.get_field_by_name('category')[0]
        translator = converter.MAPPING[type(field)]
        descriptor = translator(field)
        
        cats = Category.objects.all()
        opts = descriptor['options']
        self.assertEquals(len(opts), len(cats))
        for opt in opts:
            self.assertEquals(str(Category.objects.get(id=opt['value'])), opt['label'])  
            
    
    def test_fields_for_model(self):
        '''
        Test fields_for_model generator.
        '''
        
        field_dscs = converter.fields_for_model(News, ['name'])
        self.assertTrue(len(field_dscs)==1)
        fields = News._meta.get_all_field_names()
        fields.remove('id')
        for f in converter.fields_for_model(News, fields):
            self.check_attrs(News._meta.get_field_by_name(f['name'])[0], f)
        
        
    
    def test_form_for_model(self):
        '''
        Test form_form_model generator.
        '''
        fields = News._meta.get_all_field_names()
        fields.remove('id')
        schema = converter.form_for_model(News, fields, 'myform')
        self.assertTrue(schema.has_key('name'))
        
        for f in schema['fields']:
            self.check_attrs(News._meta.get_field_by_name(f['name'])[0], f)
        
        

class ObjectToContext(TestCase):    
    '''
    Test context generation.
    '''
    
    def check_context(self, context, obj):
        '''
        Checks that context matches to object.
        '''
        for name in obj.__class__._meta.get_all_field_names():
            val = getattr(obj, name)
            if type(obj._meta.get_field_by_name(name)[0]) in [db.models.ForeignKey]:
                val = getattr(val, 'pk')
            
            self.assertEquals(context[name], val)
    
    
    def test_obj_to_schema(self):
        cat = Category(name='q')
        cat.save()
        n = News(name='a', teaser='b', rating=1, somefloat=0.2, category=cat)
        n.save()
        context = converter.object_to_context(n)
        self.check_context(context, n)
        
        self.assertTrue(type(context['category'])==int)




        









