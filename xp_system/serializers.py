from rest_framework import serializers
from .models import XPEntry, UserProfile
from django.contrib.auth.models import User

# Serializer for XPEntry model
class XPEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = XPEntry
        fields = '__all__'

# Serializer for UserProfile model
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Optional: Serializer for User including profile
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']
