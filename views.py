from django.shortcuts import render
from .serializers import StoreSerializer, UserSerializer
from .models import Store, user
from rest_framework import generics, response, status

# Create your views here.


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'


class StoreDeleteAll(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        # Delete all Store objects
        Store.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
    
class userList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class userDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'

class userDeleteAll(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        user.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
    
