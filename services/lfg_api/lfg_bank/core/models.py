from django.db import models

class ConfigurableFields(models.Model):
    active_fields = models.JSONField(default=list)

class Proposal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    value = models.CharField(max_length=100, blank=False, null=False)
