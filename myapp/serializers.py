from rest_framework import serializers
from django.contrib.auth.models import User
from django.core import exceptions
from django.contrib.auth import password_validation as validator

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', )
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def create(self, validated_data):
    
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def validate_password(self, value):

        try:
            validator.validate_password(value)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(e.messages)
             
        return value


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'username': {'read_only': True},
        }
    
