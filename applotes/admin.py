from django.contrib import admin
from .models import RegistroCantidad

# Register your models here.

# Configuracion extra en el panel
class RegistroCantidadAdmin(admin.ModelAdmin):
    """
    multiples bd en django admin site
    https://sydjameer.medium.com/how-to-expose-your-multiple-database-for-admin-site-in-django-50a7870d14ab
    https://docs.djangoproject.com/en/dev/topics/db/multi-db/#exposing-multiple-databases-in-django-s-admin-interface
    """
    # A handy constant for the name of the alternate database.
    using = "applotes"

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
    # readonly_fields = ['id_ot', 'num_ot', 'ensamblaje', 'componente', 'semana', 'fec_registro']
    search_fields = ['num_ot']
    list_display = ['id', 'id_ot', 'num_ot', 'ensamblaje', 'componente', 'cantidad', 'semana', 'fec_registro']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si se está editando un objeto existente
            return ['id_ot', 'num_ot', 'ensamblaje', 'componente', 'semana', 'fec_registro']
        else:  # Si se está creando un objeto nuevo
            return []

admin.site.register(RegistroCantidad, RegistroCantidadAdmin)
