from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('index/', views.index, name="index"),
    path('listing/', views.listing, name="listing"),
]
