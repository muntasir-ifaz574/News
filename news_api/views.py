from django.shortcuts import render
import requests
API_KEY = '4b79f0b9f1dd4d6386efa122485ee0e4'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        responce = requests.get(url)
        data = responce.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        responce = requests.get(url)
        data = responce.json()
        articles = data['articles']

    context ={
        'articles': articles
    }
    return render(request, 'news_api/home.html', context)
