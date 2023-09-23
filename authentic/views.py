from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from authentic.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        ser_check = serializer.is_valid()
        if ser_check:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            # Создайте URL-адрес, на который вы хотите перенаправить пользователя после регистрации
            redirect_url = "  successfulreg"
            # Замените 'login' на имя URL-адреса страницы входа

            # Верните ответ с кодом 302 и заголовком Location
            response = Response(serializer.data, status=status.HTTP_302_FOUND)
            response["Location"] = redirect_url
            return response

        else:
            response = Response(serializer.data, status=status.HTTP_302_FOUND)
            return response
        # serializer.errors
        # return HttpResponse(serializer.errors)


def registr(request):
    return render(request, "authentic/registr.html")


def successfulreg(request):
    return render(request, "authentic/successfulreg.html")
