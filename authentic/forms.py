from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, label="Имя пользователя", required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, label="Пароль", required=True
    )
