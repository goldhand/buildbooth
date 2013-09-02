try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

urlpatterns = patterns('starterapp.views',
                       url(r'^nocontext/$', 'nocontext_view', name='nocontext-view'),
                       #url(r'(?<pk>)/^$', StarterAppDetailView.as_view(), name='detail-view'),
                       #url(r'^$', StarterAppListView.as_view(), name='detail-view'),
)

