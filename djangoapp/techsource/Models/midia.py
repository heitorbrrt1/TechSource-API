from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class FileExtensionValidator:
    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions

    def __call__(self, value):
        ext = value.name.split('.')[-1]
        if ext.lower() not in self.allowed_extensions:
            raise ValidationError(
                f"Somente os seguintes formatos são permitidos: {', '.join(self.allowed_extensions)}")


class Midia(models.Model):
    VIDEO = 'VI'
    IMAGEM = 'IM'

    STATUS_OPTIONS = [
        (VIDEO, 'Video'),
        (IMAGEM, 'Imagem')
    ]

    allowed_extensions = ['mp4', 'avi', 'jpg', 'jpeg', 'png', 'gif']

    nome = models.CharField(blank=True, null=True)
    tipo = models.CharField(
        max_length=2, choices=STATUS_OPTIONS, null=False, blank=False)
    anexo = models.FileField(null=False, blank=False, validators=[
                             FileExtensionValidator(allowed_extensions)])

    def __str__(self) -> str:
        return self.get_tipo_display() + ': ' + self.nome
