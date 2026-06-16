from django.urls import path

from app.views import index, name_form, greet

urlpatterns = [
   path(r'index1/', index, name='index'),
   path('name/', name_form, name='name_form'),
   path('great/', greet, name='greet'),
]