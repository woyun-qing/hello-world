from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

def search_form(request):
	return render(request,'search_form.html')

def search(request):
	request.encoding = 'utf-8'
	if 'q' in request.GET:
		message = 'the content of you serach:' + request.GET['q']
	else:
		message = 'the null you update'
	return HttpResponse(message)