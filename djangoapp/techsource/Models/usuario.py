from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractUser):
    username = models.TextField()
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True, error_messages={
                              'unique': "O email cadastrado já existe."})
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
    telefone = models.CharField(max_length=16, validators=[RegexValidator(
        regex=r'^(1[1-9]|[4689][0-9]|2[12478]|3([1-5]|[7-8])|5([13-5])|7[193-7])9[0-9]{8}$', message='O telefone deve conter no mínimo 11 números, considerando DDD e o 9 adicional, sem espaços.')], null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True,
           validators=[
               RegexValidator(
                   regex=r'^[0-9]{11}$', 
                   message='O CPF deve conter 11 números.'
               )],
            error_messages={'unique': "O CPF cadastrado já existe."})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    def __str__(self) -> str:
        return f'Nome de usuario: {self.nome} - email: {self.email}'