from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Разрешение позволяет только аутентифицированным пользователям выполнять действия,
    но позволяет всем остальным просматривать ресурсы.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
