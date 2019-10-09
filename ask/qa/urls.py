from ask.qa.views import test
from django.conf.urls import url
from views import test

urlpatterns = [
    url(r'^$', test),
]    
   
