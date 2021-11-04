from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL)


class TimestampBase(Model):
    date_created = DateTimeField(auto_now_add=True)
    date_updated = DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


# this is based on https://evileg.com/en/post/576/

# class SingletonModel(Model):
#     class Meta:
#         abstract = True
 
#     def save(self, *args, **kwargs):
#         self.__class__.objects.exclude(id=self.id).delete()
#         super(SingletonModel, self).save(*args, **kwargs)
 
#     @classmethod
#     def load(cls):
#         try:
#             return cls.objects.get()
#         except cls.DoesNotExist:
#             return cls()