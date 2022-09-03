#import time
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from django.http.response import HttpResponse
import urllib.request
#from urllib.request import urlopen
import json


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("s_scanner")

        else:
            return render(request, "login.html",{
                "error":"username ya da password yanlış"
            })
    return render(request, "login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "register.html",
                {
                    "error": "bu username kullanılıyor.",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname
                })
            elif User.objects.filter(email=email).exists():
                return render(request, "register.html",
                {
                    "error": "bu email kullanılıyor.",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname
                })
            else:
                user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                user.save()
                return redirect("login")

        else:
            return render(request, "register.html",
            {
                "error":"password ile repassword aynı değil",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })

    return render(request, "register.html")

def s_scanner_request(request):
    return render(request,"index.html")

def loadjson(request,slug):
    url = "http://127.0.0.1:8000/account/models/face_landmark_68_model-weights_manifest.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print(data)

#    with open("/models/face_landmark_68_model-weights_manifest.json", "r") as file:
#        data = json.load(file)

 #   json_data = open('/static/prices.json')
 #   data1 = json.load(json_data)  # deserialises it
 #   data2 = json.dumps(data1)  # json formatted string

  #  json_data.close()
   # json_file = "/account/models/" + file_name
   # data = open(json_file).read()
   # json.loads(data)
    #json_content = read_file(json_file)
    #return HttpResponse(
    #    json_content,
    #    content_type='application/json',
    #    status=200
    #)



def logout_request(request):
    logout(request)
    return redirect("home")

