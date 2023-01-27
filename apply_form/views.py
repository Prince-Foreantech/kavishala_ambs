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
            try:
                user = signup.objects.get(username=request.POST['username'])
                if user:
                    message = messages.error(request,'Username Already Taken')
                    return HttpResponse("User name already taken")
        
                else:
                    user = signup()
                    user.username = request.POST['username']
                    user.password = request.POST['password']
                    user.name = request.POST['name']
                    user.city = request.POST['city']
                    user.email = request.POST['email']
                    if request.POST['contact_number'] != 10:
                        return redirect('pass')
                    else:
                        user.contact_number = request.POST['contact_number']
                    user.course_year = request.POST['course_year']
                    user.save()
                    return HttpResponse("User Saved")
            except:
                message = messages.error(request,'Please try after sometime !')
                return HttpResponse("Unkown Error")
    except:
        return HttpResponse("method is not post")
@csrf_exempt
def loginValidate(request):
    try:
        if request.method=="POST":
            user = signup.objects.get(username=request.POST['username'],password=request.POST['password'])
            if user:
                if user.confirmation=='True':
                    message = messages.success('Signed In')
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