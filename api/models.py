from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    created_at = models.DateTimeField(_('DTSM1'), auto_now_add=True, null=True, blank=True, help_text=_('DTST1'))
    updated_at = models.DateTimeField(_('DTSM2'), auto_now=True, null=True, blank=True, help_text=_('DTST2'))
    name = models.CharField(_('name'), help_text=_('name'), max_length=200, unique=False)
    mobile_phone = PhoneNumberField()
    home_phone = PhoneNumberField()
    email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class Company(models.Model):
    created_at = models.DateTimeField(_('DTSM1'), auto_now_add=True, null=True, blank=True, help_text=_('DTST1'))
    updated_at = models.DateTimeField(_('DTSM2'), auto_now=True, null=True, blank=True, help_text=_('DTST2'))
    name = models.CharField(_('name'), help_text=_('name'), max_length=200, unique=False)
    supervisor_name = models.CharField(max_length=200, unique=False)
    supervisor_mobile_phone = PhoneNumberField()
    supervisor_home_phone = PhoneNumberField()
    supervisor_email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

# todo: add retail and catalog price validation
class Item(models.Model):
    created_at = models.DateTimeField(_('DTSM1'), auto_now_add=True, null=True, blank=True, help_text=_('DTST1'))
    updated_at = models.DateTimeField(_('DTSM2'), auto_now=True, null=True, blank=True, help_text=_('DTST2'))
    code = models.CharField(max_length=200, unique=False)
    catalog_price = models.DecimalField(decimal_places=2, max_digits=10)
    retail_price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField()
    client = models.ForeignKey(Client, related_name='item_client')

    def __str__(self):
        return "%s" % self.code

    def __unicode__(self):
        return "%s" % self.code

    class Meta:
        unique_together = ("code", "client")
        index_together = ("code", "client")


class Status(models.Model):
    created_at = models.DateTimeField(_('DTSM1'), auto_now_add=True, null=True, blank=True, help_text=_('DTST1'))
    updated_at = models.DateTimeField(_('DTSM2'), auto_now=True, null=True, blank=True, help_text=_('DTST2'))
    name = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class Order(models.Model):
    created_at = models.DateTimeField(_('DTSM1'), auto_now_add=True, null=True, blank=True, help_text=_('DTST1'))
    updated_at = models.DateTimeField(_('DTSM2'), auto_now=True, null=True, blank=True, help_text=_('DTST2'))
    company = models.ForeignKey(Company, related_name='order_company')
    campaign = models.CharField(max_length=200, unique=False)
    status = models.ForeignKey(Status, related_name='order_status')
    items = models.ManyToManyField(Item, related_name='order_itens')

    def __str__(self):
        return "%s - %s" % (self.company, self.campaign)

    def __unicode__(self):
        return "%s - %s" % (self.company, self.campaign)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)