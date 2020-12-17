from django.db import models


class Ingredient(models.Model):
    code = models.CharField(max_length=8, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Nome")

    def __str__(self):
        return self.name


class Pastry(models.Model):
    code = models.CharField(max_length=8, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Nome")
    value = models.FloatField(verbose_name="Valor")
    weight = models.CharField(verbose_name="Peso")
    unit = models.CharField(verbose_name="Unidade de Medida")
    obs = models.CharField(verbose_name="Observações")
    ingredients = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, verbose_name="Ingredientes")

    def __str__(self):
        return self.name

