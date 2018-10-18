from django.conf.urls import url
from editor import views

app_name = 'editor'

urlpatterns = [
    url(r'^$', views.typingEditor , name = 'typingEditor'),
]
