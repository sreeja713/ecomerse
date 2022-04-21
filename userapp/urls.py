
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('login', views.loginpage,name="loginpage"),
    path('logout', views.logoutfunc,name="logout"),
    path('usershow/<int:id>', views.usershow,name="usershow"),
    
   
    
]
