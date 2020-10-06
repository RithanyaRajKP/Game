from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home page'),
path('home/',views.home,name='home page'),
    path('about/',views.about,name='about page'),
    path('expression',views.expression,name='expression value'),
    path('nameee',views.nameee,name='name value')
]