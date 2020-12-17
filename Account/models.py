from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=150)
    email = models.EmailField(_('Email'), unique=True)
    mobile = models.CharField(_('Phone Number'), max_length=12)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    class META:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL)
    image = models.ImageField(_('Image'), upload_to='avatar')


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL)
    city = models.CharField(_('City'), max_length=70)
    street = models.CharField(_('Street'), max_length=70)
    allay = models.CharField(_('Allay'), max_length=70)
    zip_code = models.IntegerField(_('Zip Code'), )


class Shop(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL)
    slug = models.SlugField(_('Slug'), unique=True, db_index=True)
    name = models.TextField(_('name'))
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Shop Logo'), upload_to='shop-logo')


class Email(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL)
    subject = models.CharField(_('Subject'), max_length=988)
    body = models.TextField(_('body'))
