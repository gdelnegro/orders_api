from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

# Register your models here.
class CustomModelAdminMixin(object):
    def __init__(self, model, admin_site):
        # self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        # Fields from related fields, to be added in search

        super(CustomModelAdminMixin, self).__init__(model, admin_site)
        self.filter_horizontal = [field.name for field in model._meta.get_fields() if
                                  field.many_to_many and "reverse" not in str(type(field))]

        # get all fields that aren't related to another model
        self.search_fields = [field.name for field in model._meta.get_fields() if
                              not field.many_to_many and "Point" not in str(type(field)) and "related" not in str(
                                  type(field))]

        related_fields = []
        # get all fields that are related to another model
        for model_field in model._meta.get_fields():
            if not model_field.many_to_many and "related" in str(type(model_field)):
                for related_field in model_field.related_model._meta.get_fields():
                    # if the field have one of the fields from the 'related_fields_to_add' variable
                    # and one of the languages in the field name, add it to the search_fields
                    self.search_fields.append(model_field.name+"__"+related_field.name)

        self.search_fields.remove("id")


@admin.register(Client)
class ClientAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass
