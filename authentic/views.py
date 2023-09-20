from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from authentic.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # base variable to get the data below

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
        )  # serializer_class - this var help us to get data for var serializer
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            # Вернуть JSON-ответ с данными о пользователе и HTTP-статусом 201 Created
            response_data = serializer.data
            response_data["message"] = "Регистрация прошла успешно."
            # return Response(
            #     response_data, status=status.HTTP_201_CREATED, headers=headers
            # )
            return redirect("../../correctregisrt") 
        except Exception as e:
            # Если возникла ошибка при создании пользователя, вернуть JSON-ответ с ошибкой
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Добавьте здесь логику создания пользователя (может потребоваться изменить)
        serializer.save()

        # После успешной регистрации, выполнить редирект на указанный URL
        redirect_url = "./correctregisrt.html"
        return redirect(redirect_url)


def registration_view(request):
    return render(request, "authentic/registration.html")


def reg(request):
    return render(request, "authentic/correctregisrt.html")
    