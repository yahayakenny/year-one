from django.shortcuts import render
import requests
from movie_app.models import Movie

def get_movies(request): 
    if 'title' in request.GET:
        title = request.GET['title']
        url = 'http://www.omdbapi.com/?apikey=8decb275&s=%s' % title
        response = requests.get(url)
        data = response.json()
        movie = data['Search']
       
         #    https://medium.com/@chilinski.a/how-to-seed-a-django-api-with-data-from-an-external-api-b577b6e6ad54
        for i in movie:
            movie_data = Movie(
                title = i['Title']    
            )
            movie_data.save()
        

    return render(request, 'movies/index.html', {'movie': movie})



 
