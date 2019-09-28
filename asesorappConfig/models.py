from django.db import models


class Estudio(models.Model):
    titulo = models.CharField(max_length=100)
    entidad = models.CharField(max_length=100)
    estatus = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " " + self.titulo


class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_cedula = models.IntegerField()
    correo = models.CharField(max_length=100)
    numero_telefono = models.IntegerField()
    url_foto = models.CharField(max_length=1000,blank=True)
    esAbogado = models.BooleanField(default=False)
    descripcion_perfil = models.TextField(blank=True)
    estudios = models.ManyToManyField(Estudio,blank=True)

    def __str__(self):
        return str(self.id) + " " + self.nombres +" "+ self.apellidos


class Caso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " " +self.titulo


class Oferta(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True)
    tarifa_hora =  models.IntegerField(default=0)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, default=-1)
    def __str__(self):
        return str(self.id) + " [" + self.caso.titulo +"] "+ self.autor.nombres + " " + self.autor.apellidos 


class Notificacion(models.Model):
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    def __str__(self):
        return str(self.id) +" [to: " + self.destinatario.nombres +"] "+self.texto
