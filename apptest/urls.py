from django.conf.urls import *
from . import views

urlpatterns = [
    url('blog', views.post_list, name='post_list'),
	url('test_page/(?P<dato>\d+)/', views.test_page, name='test_page'),
	url('test_page/$', views.test_page, name='test_page'),
	url('test_json', views.test_json, name='test_json'),
	url('private$', views.test_autenticar, name='test_autenticar'),
	url('noautorizado/$', views.no_autorizado, name='no_autorizado'),
	url('autenticar/$', views.autenticar, name='autenticar'),
	url('upload/$', views.upload, name='upload'),
	url('upload_pdf/$', views.upload_pdf, name='upload_pdf'),
]