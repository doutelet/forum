from ask.qa.views import test
from django.conf.urls import url

    url(r'^$', )
   # TODO 
   # r'^login/', include('qa.urls')
   # |
   # v
    url(r'^login/', )
    url(r'^signup/', )
    url(r'^question/[0-9]+/', test)
    url(r'^ask/', )
    url(r'^popular/', )
    url(r'^new/', )
