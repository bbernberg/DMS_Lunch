from django.conf.urls import url, include
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', views.restaurant, name='restaurant'),
	url(r'^(?P<restaurant_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
	url('^register/', CreateView.as_view(template_name='registration/register.html', form_class=UserCreationForm), name='register'),
    url('^do-register/', views.do_register, name='do_register'),   
    url(r'^(?P<review_id>[0-9]+)/add_review_comment/$', views.add_review_comment, name='add_review_comment'),
    url(r'^(?P<restaurant_id>[0-9]+)/update_thumbs_down/$', views.update_thumbs_down, name='update_thumbs_down'),
    url(r'^(?P<restaurant_id>[0-9]+)/mark_visited/$', views.mark_restaurant_visited, name='mark_restaurant_visited'),
    url(r'^add-restaurant/', views.add_restaurant, name='add_restaurant'),
    url(r'^do-add-restaurant/', views.do_add_restaurant, name='do_add_restaurant'),
]