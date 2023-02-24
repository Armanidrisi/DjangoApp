from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.userlogin,name="login"),
    
    path('signup',views.signup,name="signup"),
    
 path('logout',views.logoutuser,name="logout")
]
