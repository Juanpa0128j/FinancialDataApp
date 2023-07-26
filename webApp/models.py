from django.db import models
import json


# Create your models here.
class Tag(models.Model):
    symbol = models.CharField(primary_key=True, max_length=10)
    short_name = models.CharField(max_length=20, null=True)
    debt_equ = models.FloatField(default=0)
    insiders = models.FloatField(default=0)
    price = models.FloatField(default=0)
    t_price = models.FloatField(default=0)
    upside = models.FloatField(default=0)
    t_pe = models.FloatField(default=0)
    f_pe = models.FloatField(default=0)
    t_eps = models.FloatField(default=0)
    f_eps = models.FloatField(default=0)
    roa = models.FloatField(default=0)
    roe = models.FloatField(default=0)
    profit_m = models.FloatField(default=0)
    my_score = models.FloatField(default=0)
    my_count = models.SmallIntegerField(default=0)


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=80)
    associated_tags = models.CharField(max_length=5000, default="[]")

    @property
    def associated_tags_list(self):
        return json.loads(self.associated_tags)

    @associated_tags_list.setter
    def associated_tags_list(self, list):
        self.associated_tags_list = json.dumps(list)
