from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    grado = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    grande = models.CharField(max_length=150)
    sobre = models.TextField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Historia(models.Model):
    nombre = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=200)
    portada = ThumbnailerImageField(
        upload_to="historia_media",
        null=True,
        blank=True,
        editable=True,)

    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historias"

    def __str__(self):
        return self.nombre


class Post(models.Model):
    historia = models.ForeignKey(Historia)
    titulo = models.CharField(max_length=140)
    texto = models.TextField()
    orden = models.PositiveIntegerField()
    fondo = ThumbnailerImageField(
        upload_to="post_media",
        null=True,
        blank=True,
        editable=True,)
    imagen = ThumbnailerImageField(
        upload_to="post_media",
        null=True,
        blank=True,
        editable=True,)
    video = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        pass
