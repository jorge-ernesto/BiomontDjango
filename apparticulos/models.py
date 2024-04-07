from django.db import models

# Create your models here.

class CorrelativoLineas(models.Model):
    formulario = models.CharField(max_length=100, null=True)
    linea = models.CharField(max_length=100)
    nomenclatura_articulo = models.CharField(max_length=5)
    ultimo_correlativo = models.IntegerField()
    usuario_registro = models.CharField(max_length=5)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_actualiza = models.CharField(max_length=5, null=True)
    fecha_actualiza = models.DateTimeField(null=True)

    class Meta:
        """
        managed = False
        Indica que Django no controlará el modelo, esto significa que no se realizarán cambios en la estructura de la tabla.
        Sin embargo, al ejecutar "python manage.py makemigrations", aún se generará el archivo de migraciones con la propiedad "managed = False".
        Puedes usar "python manage.py sqlmigrate miapp 0001" para verificar que no se ejecutará ninguna consulta SQL relacionada con esta migración.
        Si eliminas "managed = False" del archivo de migraciones generado y luego ejecutas "python manage.py sqlmigrate miapp 0001", podrás ver las consultas SQL generadas.
        """
        managed             = False
        db_table            = 'tb_correlativo_lineas'
        verbose_name        = "Correlativo linea"
        verbose_name_plural = "Correlativo lineas"
        ordering            = ['-id']
