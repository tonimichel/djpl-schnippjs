

def refine_get_urls(original):

    def get_urls():
        from django.conf.urls.defaults import url, patterns, include
        urlpatterns = patterns('',
            url('^testing/$', 'testproduct.views.testing', name='testing'),
        )
        return urlpatterns + original()
    return get_urls
