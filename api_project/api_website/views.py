from django.shortcuts import render
import requests

# Create your views here.
def movies_list(request):
	query = request.GET.get("qkey")
	url = 'http://www.omdbapi.com/?s=django&apikey=2999fbb4'
	
	if query:
		url='http://www.omdbapi.com/?&apikey=2999fbb4&s=' + query
	response = requests.get(url)

	context = {
		"movies" : response.json()

	}
	return render(request, 'movies_list.html', context)

def movie_detail(request, movie_id):
	url = 'http://www.omdbapi.com/?&apikey=2999fbb4&i=' + movie_id
	response = requests.get(url)
	context = {
		"movies" : response.json()

	}
	return render(request, 'movie_detail.html', context)