from django.contrib import admin
from .models import CorrelativoLineas

# Register your models here.

# Configuracion extra en el panel
class CorrelativoLineasAdmin(admin.ModelAdmin):
    """
    multiples bd en django admin site
    https://sydjameer.medium.com/how-to-expose-your-multiple-database-for-admin-site-in-django-50a7870d14ab
    https://docs.djangoproject.com/en/dev/topics/db/multi-db/#exposing-multiple-databases-in-django-s-admin-interface
    """
    # A handy constant for the name of the alternate database.
    using = "apparticulos"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )

    """
    Configuracion en Django admin site
    """
    search_fields = ('formulario', 'linea', 'nomenclatura_articulo')
    list_display = ('id', 'formulario', 'linea', 'nomenclatura_articulo', 'ultimo_correlativo', 'usuario_registro', 'fecha_registro', 'usuario_actualiza', 'fecha_actualiza')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si se está editando un objeto existente
            return ('id', 'formulario', 'linea', 'nomenclatura_articulo', 'usuario_registro', 'fecha_registro', 'usuario_actualiza', 'fecha_actualiza')
        else:  # Si se está creando un objeto nuevo
            return ()

    def has_add_permission(self, request):
        # Restringe la capacidad de agregar registros
        return False

    def has_delete_permission(self, request, obj=None):
        # Restringe la capacidad de eliminar registros
        return False

admin.site.register(CorrelativoLineas, CorrelativoLineasAdmin)
