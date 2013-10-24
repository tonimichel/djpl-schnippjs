from django.test import LiveServerTestCase
from selenium import webdriver
from testproduct.models import Category, News

class MySeleniumTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test(self):
        '''
        Tests that the generated schema and context are compatible with a javscript schnippform.
        views.testing (/testing/) renders a view with two forms of the same model - one with data (context)
        and the other without. 
        Checks that the schnippform renders as expected => the generated format is correct.
        Checks that the other schnippforms fields provide initial values accoording to the passed context.
        '''
        cat = Category(name='Coding')
        cat.save()
        n = News(name='Djangoproductline', teaser='productivity', rating=1, somefloat=62.8, category=cat)
        n.save()
        self.browser.get(self.live_server_url + '/testing/')
        
        # check that all fields are rendered in #a
        target_a = self.browser.find_element_by_id('a')
        for field in News._meta.fields:
            if field.name != 'id':
                target_a.find_element_by_xpath('//label[text()="%s"]' % field.verbose_name)       
        
        
        # check that all fields are rendered in #b
        target_b = self.browser.find_element_by_id('b')
        for field in News._meta.fields:
            if field.name != 'id':
                target_b.find_element_by_xpath('//label[text()="%s"]' % field.verbose_name)
        # check that context loading was works
        target_b.find_element_by_xpath('//div[@class="schnippforms-dropdownselect-display" and text()="%s"]' % str(cat))
        target_b.find_element_by_xpath('//input[@name="somefloat" and @value="%s"]' % n.somefloat)
        
        
        
