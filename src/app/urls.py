from django.urls import path

from app.views import index, name_form, greet, profile_form, customers, api_comments, api_products

urlpatterns = [
   path(r'index1/', index, name='index'),
   path('name/', name_form, name='name_form'),
   path('great/', greet, name='greet'),
   path('profile/', profile_form, name='profile_form'),
   path('customers/', customers, name='customers'),
   path('comments/', api_comments, name='comments'),
   path('products/', api_products, name='api_products')
]