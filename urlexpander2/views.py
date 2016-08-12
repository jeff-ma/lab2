from .models import Url_Address
from django.shortcuts import render, get_object_or_404
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
import requests
import json

# Create your views here.

@login_required(login_url="/expander2/login/")
def index(request):
    url_list = Url_Address.objects.all()
    return render(request, 'urlexpander2/index.html', {'url_list' : url_list})

@login_required(login_url="/expander2/login/")
def expand(request):
	shorter_url = request.POST['shorter_url']
	html = urlopen(shorter_url)
	soup = BeautifulSoup(html, 'html.parser')
	url = Url_Address()
	url.short_url = shorter_url
	url.full_url = html.geturl()
	url.http_status = html.getcode()
	url.page_title = soup.html.head.title.contents[0]
	wayback_api = "https://archive.org/wayback/available?url=" + url.full_url
	response = requests.get(wayback_api)
	data = response.json()
	if len(data['archived_snapshots']) > 0:
		url.wayback_url = data['archived_snapshots']['closest']['url']
		url.timestamp = data['archived_snapshots']['closest']['timestamp']
	url.save()
	url_list = Url_Address.objects.all()
	return render(request, 'urlexpander2/index.html', {'url_list' : url_list})

@login_required(login_url="/expander2/login/")
def delete(request, url_pk):
	url = get_object_or_404(Url_Address, pk=url_pk)
	url.delete()
	url_list = Url_Address.objects.all()
	return render(request, 'urlexpander2/index.html', {'url_list' : url_list})
