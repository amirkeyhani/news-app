from django.shortcuts import render
import requests
from django.core.paginator import Paginator
# Create your views here.


def news(request):
    url = (f'https://newsapi.org/v2/top-headlines?'
           'sources=bbc-news&'
           'apiKey=0d4d6b3c438d48809c5f668175d92820')
    response = requests.get(url).json()
    author = []
    title = []
    description = []
    url = []
    image = []
    publishAt = []

    for i in range(len(response['articles'])):
        author.append(response['articles'][i]['author'])
        title.append(response['articles'][i]['title'])
        description.append(response['articles'][i]['description'])
        url.append(response['articles'][i]['url'])
        image.append(response['articles'][i]['urlToImage'])
        publishAt.append(response['articles'][i]['publishedAt'])

    headline_url = (r'https://newsapi.org/v2/top-headlines?'
                    'country=us&'
                    'apiKey=0d4d6b3c438d48809c5f668175d92820')
    headline_response = requests.get(headline_url).json()
    headline_author = []
    headline_title = []
    headline_description = []
    headline_url = []
    headline_image = []
    headline_publishAt = []

    for i in range(6):
        headline_author.append(headline_response['articles'][i]['author'])
        headline_title.append(headline_response['articles'][i]['title'])
        headline_description.append(
            headline_response['articles'][i]['description'])
        headline_url.append(headline_response['articles'][i]['url'])
        headline_image.append(headline_response['articles'][i]['urlToImage'])
        headline_publishAt.append(
            headline_response['articles'][i]['publishedAt'])

    News = list(zip(author, title, description, url, image, publishAt))
    headline = list(zip(headline_author, headline_title, headline_description,
                    headline_url, headline_image, headline_publishAt))
    paginator = Paginator(News, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', context={'news': page_obj, 'headline': headline})
