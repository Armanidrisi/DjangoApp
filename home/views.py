from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
  #print(request.user)
  if request.user.is_anonymous:
        return redirect("/login") 
  return render(request,"index.html")

def userlogin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      print("Not Found")
      return render(request,"login.html")
  return render(request,"login.html")
  
def signup(request):
  if request.method == "POST":
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
  return render(request,"register.html")
  
def logoutuser(request):
    logout(request)
    return redirect('/')