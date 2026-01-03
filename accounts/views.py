from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login, logout

# Authenticating information and storing user during registration
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'User created successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Implementing login.
# Using Djnago's defualt authenticate mechanism to verify users and create session once user is verified.
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message":"Login successfull"})
        return Response(
            {"message":"Invalid username or Password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message":"User logged out successfully"})

