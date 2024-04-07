from django.db import models

# Create your models here.

class RegistroCantidad(models.Model):
    id_ot = models.IntegerField()
    num_ot = models.CharField(max_length=6)
    ensamblaje = models.CharField(max_length=10)
    componente = models.CharField(max_length=10)
    cantidad = models.DecimalField(max_digits=11, decimal_places=5)
    semana = models.CharField(max_length=40)
    fec_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        managed = False
        Indica que Django no controlará el modelo, esto significa que no se realizarán cambios en la estructura de la tabla.
        Sin embargo, al ejecutar "python manage.py makemigrations", aún se generará el archivo de migraciones con la propiedad "managed = False".
        Puedes usar "python manage.py sqlmigrate miapp 0001" para verificar que no se ejecutará ninguna consulta SQL relacionada con esta migración.
        Si eliminas "managed = False" del archivo de migraciones generado y luego ejecutas "python manage.py sqlmigrate miapp 0001", podrás ver las consultas SQL generadas.
        """
        managed             = False
        db_table            = 'tb_registro_cantidad_test'
        verbose_name        = "Registro cantidad"
        verbose_name_plural = "Registro cantidades"
        ordering            = ['-id']
