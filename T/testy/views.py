from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods  
import datetime   


def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse  
 
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')  