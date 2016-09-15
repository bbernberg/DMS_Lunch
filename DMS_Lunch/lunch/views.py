from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from lunch.models import Restaurant, Review

@login_required
def dashboard(request):
	return HttpResponse("DMS Lunch Dashboard ({})".format(request.user.username))

@login_required
def restaurant(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	return render(request, 'lunch/restaurant.html', {'restaurant': restaurant})

def add_review(request, restaurant_id):
	if request.user:
		print ("User added review = {}".format(request.user))
	else:
		"No user logged in"
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	review = Review(text=request.POST['new_review'], date=timezone.now(), restaurant=restaurant)
	return HttpResponseRedirect(reverse('restaurant', args=restaurant_id))

def do_register(request):
	user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
	auth_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
	login(request, auth_user)
	return HttpResponseRedirect(reverse('dashboard'))
