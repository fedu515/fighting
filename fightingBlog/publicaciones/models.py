from django.db import models

class Posteo(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion= models.TextField(null = True)


class Video(models.Model): #los videos no se descargan solo se visualizan
    nombreVideo= models.CharField(max_length=100)
    descripcion= models.TextField(null = True)
    
    

class Audio(models.Model): #los audios se descargan o se reproducen
    nombreAudio = models.CharField(max_length=100)
    descripcion = models.TextField(null = True)
    


class Archivo(models.Model): #
    nombreArchivo = models.CharField(max_length=50)
    descripcion = models.TextField(null = True)
    