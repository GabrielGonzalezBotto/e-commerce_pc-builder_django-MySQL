from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from  .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(required=True, label="Nombre/s")
    last_name = forms.CharField(required=True, label="Apellido/s")

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'telefono', 'postal', 'direccion']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    
class LoginForm(AuthenticationForm):
    pass