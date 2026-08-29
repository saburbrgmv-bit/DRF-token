from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializers, LoginSerializer, MySerializers

class RegisterAPIView(APIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]

    @extend_schema(tags=['Users'], description='Siz bu API orqali register qila olasiz (username va password)', summary='rigister api')
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # ИСПРАВЛЕНО: добавлен .data, чтобы вернуть сериализованный JSON
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @extend_schema(tags=['Users'],  summary='login api')
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token':token.key, 'username':user.username})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyAPIView(APIView):
    serializer_class = MySerializers
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Users'],  summary='My api')
    def get(self, request):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data)

    @extend_schema(tags=['Users'],  summary='My post api')
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)




