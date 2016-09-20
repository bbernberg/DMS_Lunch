from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from lunch.models import Restaurant, Review, ReviewComment

@login_required
def dashboard(request):
	restaurants = Restaurant.objects.exclude(thumbs_down_by_users__pk=request.user.pk)
	visited_restaurants = list()
	unvisited_restaurants = list()
	for restaurant in restaurants:
		if restaurant.visited:
			visited_restaurants.append(restaurant)
		else:
			unvisited_restaurants.append(restaurant)
	thumbs_down_restaurants = Restaurant.objects.filter(thumbs_down_by_users__pk=request.user.pk)
	return render(request, 'lunch/dashboard.html', 
		{'user': request.user, 
		'visited_restaurants': visited_restaurants, 
		'unvisited_restaurants': unvisited_restaurants,
		'thumbs_down_restaurants': thumbs_down_restaurants})

@login_required
def restaurant(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	reviews = Review.objects.filter(restaurant__pk=restaurant_id)
	thumbs_down = restaurant.thumbs_down_by_users.all().filter(pk=request.user.pk).exists()
	return render(request, 'lunch/restaurant.html', 
		{'restaurant': restaurant, 
		'reviews': reviews, 
		'thumbs_down': thumbs_down})

def add_review(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	review = Review(text=request.POST['new_review'], date=timezone.now(), restaurant=restaurant, author=request.user)
	review.save()
	return HttpResponseRedirect(reverse('restaurant', args=restaurant_id))

def add_review_comment(request, review_id):
	review = get_object_or_404(Review, pk=review_id)
	review_comment = ReviewComment(text=request.POST['new_review_comment'], 
		date=timezone.now(), 
		parent_review=review, 
		author=request.user)
	review_comment.save()
	review.comments.add(review_comment)
	review.save()
	return HttpResponseRedirect(reverse('restaurant', args=str(review.restaurant.pk)))

def do_register(request):
	user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
	auth_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
	login(request, auth_user)
	return HttpResponseRedirect(reverse('dashboard'))

def update_thumbs_down(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	if restaurant.thumbs_down_by_users.all().filter(pk=request.user.pk).exists():
		restaurant.thumbs_down_by_users.remove(request.user)
	else:
		restaurant.thumbs_down_by_users.add(request.user)
	restaurant.save()
	return HttpResponseRedirect(reverse('restaurant', args=restaurant_id))

def mark_restaurant_visited(request, restaurant_id):
	restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
	restaurant.visited = True
	restaurant.save()
	return HttpResponseRedirect(reverse('restaurant', args=restaurant_id))

@login_required
def add_restaurant(request):
	return render(request, 'lunch/add_restaurant.html')	

def do_add_restaurant(request):
	restaurant = Restaurant(name=request.POST['name'], address=request.POST['address'])
	restaurant.save()
	return HttpResponseRedirect(reverse('dashboard'))

