from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer


# GET /api/users/me/ – Return authenticated user profile
# PUT /api/users/me/ – Update profile fields (e.g., bio, avatar)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# POST /api/users/register/ – Create a new user with XP, Level, Rank
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
