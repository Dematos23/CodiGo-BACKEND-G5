from django.db import models
from django.db.models.deletion import PROTECT, SET_NULL

# Create your models here.

class PersonaModel(models.Model):

    opcionesEstadoCivil = [
        ('SOLTERO', 'SOLTERO'),
        ('CASADO', 'CASADO'),
        ('VIUDO', 'VIUDO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('COMPLICADO', 'COMPLICADO'),]

    personaId = models.AutoField(
        primary_key=True, 
        unique=True, 
        null=False, 
        db_column='id')

    personaNombre = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='nombre')

    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido')

    personaEmail = models.EmailField(
        max_length=50,
        db_column='email',
        null=False,
        unique=True)
    
    personaFechaNacimiento = models.DateField(
        db_column='fec_nac',)

    personaEstadoCivil = models.CharField(
        max_length=50,
        db_column= 'estado_civil',
        choices= opcionesEstadoCivil,
        default='NO_ESPECIFICA')

    personaFoto = models.ImageField(
        db_column = 'foto',
        upload_to = 'personas/',
        null= True,)

    class Meta:
        db_table = 'personas'
        # ordering= ['-email', 'apellido']

class CitaModel(models.Model):

    opcionesEstado = [
        ('ACTIVA','ACTIVA'),
        ('CANCELADA','CANCELADA'),
        ('POSPUESTA','POSPUESTA'),
    ]

    citaID = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id')

    citaDescripcion = models.TextField(
        db_column='descripcion',
        null=False)

    citaFecha = models.DateTimeField(
        db_column='fecha',
        null=False)

    citaLatitud = models.FloatField(
        db_column='latitud',
        null=False)

    citaLongitud = models.FloatField(
        db_column='longitud',
        null=False)

    citaEstado = models.CharField(
        max_length=50,
        choices= opcionesEstado,
        db_column='estado',
        null=False)

    createdAt = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True)

    updatedAt = models.DateTimeField(
        db_column='updated_at',
        auto_now_add=True)

    citador = models.ForeignKey(
        to=PersonaModel,
        db_column='citador_id',
        on_delete=models.PROTECT,
        related_name='personaCitas'
    )

    citado = models.ForeignKey(
        to = PersonaModel,
        db_column='citado_id',
        on_delete=models.PROTECT,
        related_name='personaCitadas'
    )

    class Meta:

        db_table = 'citas'
        unique_together = [['citaFecha', 'citador'], ['citaFecha', 'citado']]
        ordering=['-citaFecha']