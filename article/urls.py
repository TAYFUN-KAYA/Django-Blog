from django.contrib import admin
from django.urls import path
from article import views

app_name="article"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('comment/<int:id>',views.comment,name="comment"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('',views.articles,name="article")
]
