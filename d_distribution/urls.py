from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='start_page'),
    url(r'getDistribution/', views.post, name='get_distribution'),
]