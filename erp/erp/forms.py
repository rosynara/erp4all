from django import forms
from django.forms import widgets

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuário', max_length=100, required=True, widget=forms.TextInput) #, error_messages={"required":"Informe o usuário."}
    senha = forms.CharField(label='Senha',max_length=100, required=True, widget=forms.PasswordInput)

