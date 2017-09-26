from django.http import HttpResponse
from TestModel.models import Test
def testdb(request):
	test1 = Test(name='runoob1')
	test1.save()
	return HttpResponse('<p>the data is update</p>')

def testdbget(request):
	response =''
	response1 = ''
	list = Test.objects.all()
	for var in list:
		response1 = response1 + var.name + '<br>'
		response = response1
	return HttpResponse('<p>' + response + '</p>'+'<br>'+'<h4>this</h4>')