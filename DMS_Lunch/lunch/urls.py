from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', views.restaurant, name='restaurant'),
	url(r'^(?P<restaurant_id>[0-9]+)/add_review/$', views.add_review, name='add_review')
]