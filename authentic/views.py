from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from authentic.serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            # Получите пользователя, которого только что зарегистрировали
            user = serializer.instance

            # Создайте или получите токен для пользователя
            token, created = Token.objects.get_or_create(user=user)
            # Создайте URL-адрес, на который вы хотите перенаправить пользователя после регистрации
            redirect_url = "successfulreg"
            # Замените 'login' на имя URL-адреса страницы входа

            response_data = {"data": serializer.data, "token": token.key}
            # Верните ответ с кодом 302 и заголовком Location
            response = Response(response_data, status=status.HTTP_302_FOUND)
            response["Location"] = redirect_url
            return response
        else:
            return render(request, "authentic/registr.html", {"form": serializer})


def registr(request):
    return render(request, "authentic/registr.html")


def successfulreg(request):
    return render(request, "authentic/successfulreg.html")


def log(request):
    return render(request, "authentic/autorize.html")


class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return Response(
                    {"message": "Вход выполнен успешно."}, status=status.HTTP_200_OK
                )
            else:
                print(username, password)
                return Response(
                    {"message": "Неверное имя пользователя или пароль."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
