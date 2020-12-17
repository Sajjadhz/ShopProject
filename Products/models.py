from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class ShopProduct(models.Model):
    shop = models.ForeignKey('account')
