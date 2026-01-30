from rest_framework import serializers
from .models import Store, user


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['user_id', 'user_name', 'user_email']


        
