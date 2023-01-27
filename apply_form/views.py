from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import json
from  django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from apply_form.models import signup
from .serializers import user
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def user_signup(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
            try:
                user = signup.objects.get(username=data['username'])
                if user:
                    return HttpResponse("User name already taken")
            except:
                try:
                    user = signup()
                    user.username = data['username']
                    user.password = data['password']
                    user.name = data['name']
                    user.city = data['city']
                    user.email = data['email']
                    user.contact_number=data['contact_number']
                    user.course_year = data['course_year']
                    user.college_name = data['college_name']
                    user.instagram_url = data['instagram_url']
                    user.twitter_url = data['twitter_url']
                    user.facebook_url = data['facebook_url']
                    user.save()
                    return HttpResponse("User Saved")
                except:
                    return HttpResponse("Signup Error data not getting")
    except:
        return HttpResponse("Unkown Error")
                
@csrf_exempt
def loginValidate(request):
    try:
        if request.method=="POST":
            body_unicode = request.body.decode("utf-8")
            data = json.loads(body_unicode)
            user = signup.objects.get(username=data['username'],password=data['password'])
            if user:
                return HttpResponse("User Matched")
            else:
                return HttpResponse("Wait for confirmation")
    except:
        return HttpResponse("Please try after sometime")

def getAllUser(request):
    users = signup.objects.all()
    alluser = user(users, many=True)
    userdata = JSONRenderer().render(alluser.data)
    return HttpResponse(userdata, content_type='application/json')