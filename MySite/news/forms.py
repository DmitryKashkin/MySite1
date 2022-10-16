from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

from django.core.mail import send_mail

from .models import News


class ContactForm(forms.Form):
    recipient = forms.EmailField(label='Кому:', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(
        label='Тема:',
        help_text='Не более 150 символов',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Сообщение',
    )

    def send(self, request):
        mail = send_mail(
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.cleaned_data['recipient'], ],
            fail_silently=True,
        )
        if mail:
            messages.success(request, 'Письмо отправлено')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        help_text='Не более 150 символов',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label='Email:', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Подтверждение пароля:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя:',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выбeрите категорию'

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
