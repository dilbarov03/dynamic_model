from django.db import models
from django.apps import apps


class DynamicClassMeta(models.base.ModelBase):
    def __new__(cls, name, bases, attrs, num_args=3):
        attrs['__module__'] = __name__
        new_class = super().__new__(cls, name, bases, attrs)
        return new_class

# from django.contrib import admin
# admin.site.register(model, admin_options)


# DynamicModel = DynamicClassMeta('DynamicModel', (models.Model,), {"first_name": models.CharField(max_length=15), "age": models.IntegerField()})

# from django.core.management import call_command
# call_command('makemigrations')
# call_command('migrate')



