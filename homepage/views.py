from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import blog
import json
# Create your views here.
def blog_upload(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode("utf-8")
            data = json.loads(body_unicode)
            blog_details = blog()
            blog_details.title = data['title']
            blog_details.image = data['image']
            blog_details.description = data['description']
            blog_details.url = data['url']
            blog.save()
            return HttpResponse("Blog uploaded")
        else:
            return HttpResponseBadRequest("Error in details")
    except:
        return HttpResponseBadRequest("Server Error")
