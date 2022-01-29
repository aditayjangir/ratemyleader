from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('likepost',views.like_post,name="likepost"),
    path('politician_details', views.politiciandetails, name="politiciandetails"),
]