import json
from django.http import HttpResponse, HttpResponseBadRequest
from apply_form.models import signup
from .serializers import user
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def user_signup(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
            try:
                user = signup.objects.get_queryset(email=data['email'])
                if user:
                    return HttpResponseBadRequest("User has been registered")
            except:
                try:
                    msg = None
                    user = signup()
                    if not data['username']:
                        msg = "enter a user name"
                        return HttpResponseBadRequest(msg)
                    else:
                        user.username = data['username']
                    if not data['password']:
                        msg = "Enter a password"
                        return HttpResponseBadRequest(msg)
                    elif len(data['password']) < 8:
                        msg="Password must be greater than 8 Characters"
                        return HttpResponseBadRequest(msg)
                    else:
                        user.password = data['password']
                    user.name = data['name']
                    user.city = data['city']
                    if not data['email']:
                        msg = "Please enter email id"
                        return HttpResponseBadRequest(msg)
                    else:
                        user.email = data['email']
                    if not data['contact_number']:
                        msg = "Enter contact number"
                        return HttpResponseBadRequest(msg)
                    elif len(data['contact_number']) != 10:
                        msg = "Enter a valid number"
                        return HttpResponseBadRequest(msg)
                    else:
                        user.contact_number=data['contact_number']
                    user.course_year = data['course_year']
                    user.college_name = data['college_name']
                    user.instagram_url = data['instagram_url']
                    user.twitter_url = data['twitter_url']
                    user.facebook_url = data['facebook_url']
                    user.save()
                    return HttpResponse("User Saved")
                except:
                    return HttpResponseBadRequest("Signup Error Not getting proper data")
    except:
        return HttpResponseBadRequest("Unkown Error")
                
@csrf_exempt
def loginValidate(request):
    try:
        if request.method=="POST":
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
            users = signup.objects.get(username=data['username'],password=data['password'])
            if users:
                token = get_tokens_for_user(users)
                alluser = user(users)
                userdata = JSONRenderer().render(alluser.data)
                response_data = {"data":userdata.decode(),"token":token}
                data_token = json.dumps(response_data)
                return HttpResponse(data_token,content_type="application/json")
            else:
                return HttpResponseBadRequest("Username or password Incorrect")
    except:
        return HttpResponseBadRequest("Please try after sometime")
def logout(request):
    del request.session['user_token']
    return HttpResponse("User Logout")

def getAllUser(request):
    if request.session.has_key('user_token'):
        print("pooht")
        users = signup.objects.all()
        alluser = user(users, many=True)
        userdata = JSONRenderer().render(alluser.data)
    return HttpResponse(userdata, content_type='application/json')



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
