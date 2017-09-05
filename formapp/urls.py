from django.conf.urls import url
from formapp import views as formapp_views

urlpatterns = [
	url(r'^$', formapp_views.home, name='home'),
	url(r'^create_form/$', formapp_views.create_form, name='create_form'),
	url(r'^form_edit/$', formapp_views.form_edit, name='form_edit'),
	url(r'^form_detail/(?P<pk>\d+)$', formapp_views.FormDetailView.as_view(), name='form_detail'),
]
