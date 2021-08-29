from typing import final
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Article 
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#scraping

import os 
import bs4
from bs4 import BeautifulSoup
import urllib.request


#paginacija

from django.core.paginator import Paginator




# dio za scraping 

req = urllib.request.urlopen('https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US')
xml = BeautifulSoup(req,'xml')



article = xml.findAll('item')[1:]
news = []

for i in article:
    
    if "AAPL" or "TWTR" or "GC=F(GOLD)" or "INTC" in article:
        news.append(i.text)
    else:
        print("no financial news")



# dio za main page

def index(request):
    
    #paginacija
    
    p = Paginator(xml(),4)
    page = request.GET.get('page')
    venues = p.get_page(page)


    return render(request,'index.html',{'news':news,'venues':venues})


#izlistavanje članaka i postavljanje u rest frameworku

@api_view(['GET','POST'])
def article_list(request):
    
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)

        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


#informacije za pojedinačne članke

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):

    try: 
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)