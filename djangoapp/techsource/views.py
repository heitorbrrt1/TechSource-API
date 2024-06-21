from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from techsource.Models.usuario import Usuario
from techsource.serializers import UsuarioSerializer

def index(request):
    return render(request, 'techsource/index.html')

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Usuario):
            return obj == request.user or request.user.is_staff
        return False

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes_by_action = {
        'create': [AllowAny],
        'list': [IsAdminUser],
        'retrieve': [IsOwnerOrAdmin],
        'update': [IsOwnerOrAdmin],
        'partial_update': [IsOwnerOrAdmin],
        'destroy': [IsOwnerOrAdmin]
    }
    filter_backends = [OrderingFilter]

    def perform_update(self, serializer):
        serializer.save()
        if 'password' in serializer.validated_data or 'email' in serializer.validated_data:
            login(self.request, serializer.instance)

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
