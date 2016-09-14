from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from lunch.models import Restaurant

def dashboard(request):
	return HttpResponse("DMS Lunch Dashboard")

def restaurant(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	return render(request, 'lunch/restaurant.html', {'restaurant': restaurant})

def add_review(request, restaurant_id):
	print("Review added for {} with text {}".format(restaurant_id, request.POST['new_review']))
	return HttpResponseRedirect(reverse('restaurant', args=restaurant_id))
