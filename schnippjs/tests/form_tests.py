from django.test import TestCase
from schnippjs.schnippforms.forms import SchnippForm
from django import forms
from schnippjs import schnippforms
from schnippjs.schnippforms import schnippfields
from testproduct import models



class FooForm(SchnippForm):
    some_name = forms.CharField(max_length=222)
    some_text = forms.CharField(widget=forms.Textarea)
    some_int = forms.IntegerField()
    some_float = forms.FloatField()
    some_modelchoice = forms.ModelChoiceField(queryset=models.News.objects.all())
    some_date = forms.DateField()

class schnippformsTests(TestCase):
    '''
    Test schnippform generation.
    '''
    def check_attrs(self, name, field, descriptor):
        '''
        Ensure that descriptor has the supposed fields.
        '''
        if field.label:
            self.assertEquals(descriptor['label'], field.label)
        else:
            self.assertEquals(descriptor['label'], name)
        if field.help_text:
            self.assertEquals(descriptor['description'], field.help_text)
        if field.initial:
            self.assertEquals(descriptor['default_value'], field.initial)
        if field.required:
            self.assertTrue(descriptor['required'])


    def test_field_types(self):
        '''
        Iterate all fields of the test form and check that they
        exist in the MAPPING; check the resulting descriptor attrs.
        '''
        form = FooForm()
        for name, field in form.fields.items():
            translator = schnippforms.PREPARED_FIELDS[(type(field), type(field.widget))]
            descriptor = translator(name, field)
            self.check_attrs(name, field, descriptor)
        
    
    def test_get_fields(self):
        '''
        Test get_fields translator.
        '''
        form = FooForm()
        schnields = schnippforms.get_fields(form)
        self.assertEquals(len(schnields), len(form.fields.keys()))
        
        for schnield in schnields:
            self.check_attrs(schnield['name'], form.fields[schnield['name']], schnield)
        
    def test_get_schema(self):
        '''
        Test get_schema translator.
        '''
        form = FooForm()
        schema = schnippforms.get_schema(form, 'FooForm')
        self.assertTrue(schema.has_key('name'))
        for schnield in schema['fields']:
            self.check_attrs(schnield['name'], form.fields[schnield['name']], schnield)
            
            
    
    def test_field_descriptor(self):
    
        field = forms.CharField(max_length=1, initial=2)
        default = None
        schnield = schnippfields.field_descriptor('test', field, default)
        self.assertEquals(schnield['default_value'], 2)
        
        default = 10
        schnield = schnippfields.field_descriptor('test', field, default)
        self.assertEquals(schnield['default_value'], default)
        
        
    
    def test_schema_generation_with_default_passed_as_context(self):
        schema = schnippforms.get_schema(FooForm(), 'hansi', dict(some_name='schnippjs', some_int=5))
        field = schnippforms.get_field_from_schema('some_name', schema)
        self.assertEquals(field['default_value'], 'schnippjs')
        field = schnippforms.get_field_from_schema('some_int', schema)
        self.assertEquals(field['default_value'], 5)
        
        
    
    def test_get_field_from_schema(self):
        schema = schema = schnippforms.get_schema(FooForm(), 'hansi')
        field = schnippforms.get_field_from_schema('some_name', schema)
        self.assertEquals(field['name'], 'some_name')
        
        
        
    def test_get_schema_with_formclass_instead_of_instance(self):
        self.assertRaises(
            schnippforms.FormInstancesOnly,
            schnippforms.get_schema,
            FooForm,
            'testformname'
        )        
            
            
            

        
        
class TestModelChoiceField(TestCase):

    def test(self):
        '''
        Test the modelchoicefield schnipp translation
        '''
        for i in range(0, 3):
            c = models.Category(name='Cat-%s' % i)
            c.save()
        
        class BarForm(forms.Form):
            some_modelchoice = forms.ModelChoiceField(queryset=models.Category.objects.all())
        
        form = BarForm()
        schema = schnippforms.get_schema(form, 'mybarform')

        for f in schema['fields']:
            if f['name'] == 'some_modelchoice':
                self.assertEquals(
                    len(f['options']),
                    models.Category.objects.all().count()
                )
                for o in f['options']:
                    self.assertEquals(o['label'], str(models.Category.objects.get(id=o['value'])))
                break
                
        
        form = BarForm({'some_modelchoice': 1})
        form.is_valid()
        self.assertEquals(
            type(form.cleaned_data['some_modelchoice']),
            models.Category
        )
                
        
            
class FormTest(TestCase):

    def test(self):
    
        class BarForm(forms.Form):
            name = forms.CharField(max_length=111, required=False)
            text = forms.CharField(widget=forms.Textarea)
    
        f = BarForm({'name': 'toni',  'text': 'ugug'})
        self.assertTrue(f.is_valid())
        self.assertEquals(f.cleaned_data['name'], 'toni')
        
        f = BarForm({'text': 'ugug'})
        self.assertTrue(f.is_valid())
        self.assertEquals(f.cleaned_data['text'], 'ugug')
        
        f = BarForm({'name': 'toni',  })
        self.assertFalse(f.is_valid())

        

class ModelFormTest(TestCase):

    def test(self):        
        class BarForm(forms.ModelForm):
            class Meta:
                model = models.News
        
        form = BarForm()
        schema = schnippforms.get_schema(form, 'barform')
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
    
