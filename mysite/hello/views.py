from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myview(request):
    count = request.session.get('view_count', 0)

    request.session['view_count'] = count+1

    if (count > 4):
        del request.session['view_count']
    response = HttpResponse("total view count is "+str(count))
    response.set_cookie('dj4e_cookie', 'c50467ff', max_age=1000)
    return response
