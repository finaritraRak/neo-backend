# apps/users/serializers.py
from rest_framework import serializers
from .models import User
from django.utils.text import slugify

class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 
            'role', 'status', 'last_login', 'created_at',
            'avatar', 'avatar_url', 'password'
        ]

    def get_avatar_url(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None

    def validate(self, data):
        if self.instance is None:  # création
            if not data.get('first_name'):
                raise serializers.ValidationError({"first_name": "Ce champ est requis."})
            if not data.get('last_name'):
                raise serializers.ValidationError({"last_name": "Ce champ est requis."})
            if not data.get('password'):
                raise serializers.ValidationError({"password": "Ce champ est requis."})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        base_username = ''
        if validated_data.get('first_name') and validated_data.get('last_name'):
            base_username = slugify(f"{validated_data['first_name']}.{validated_data['last_name']}")
        elif validated_data.get('email'):
            base_username = slugify(validated_data['email'].split('@')[0])
        else:
            base_username = 'user'

        username = base_username
        suffix = 0
        while User.objects.filter(username=username).exists():
            suffix += 1
            username = f"{base_username}{suffix}"

        validated_data['username'] = username

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance