from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	context = {}
	context['titlett'] = 'hello world'
	context['title2'] = 'hi world'
	return render(request,'index.html',context)

def detail(request):
	return render(request,'detail.html')

def chapter(request):
	return render(request,'chapter.html')

def more(request):
	return render(request,'more.html')

def search(request):
	return render(request,'search.html')