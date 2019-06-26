from django.urls import path

from mSite import views

urlpatterns = [
    path('', views.web),
]
