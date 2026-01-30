from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('api/stores/', views.StoreList.as_view()),
     path('api/stores/<int:store_id>/',
         views.StoreDetailUpdateDelete.as_view(), name='store_detail'),
     path('api/stores/deleteAll/', views.StoreDeleteAll.as_view(),
         name='store_delete_all'),
     path('api/users/', views.userList.as_view()),
     path('api/users/<int:user_id>/',
         views.userDetailUpdateDelete.as_view(), name='user_detail'),
     path('api/users/deleteAll/', views.userDeleteAll.as_view(),
           name='user_delete_all'),     
]
