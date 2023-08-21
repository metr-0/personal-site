import json

from django.db import models


class Settings(models.Model):
    class Meta:
        verbose_name = 'settings'
        verbose_name_plural = 'settings'

    background_image = models.ImageField(verbose_name='background-image')
    icon = models.ImageField(verbose_name='icon')

    title = models.TextField(verbose_name='title', max_length=255, blank=True)
    name = models.TextField(verbose_name='name', max_length=255, blank=True)
    description_json_array = models.TextField(verbose_name='description-json-array', blank=True)

    def description_array(self):
        return json.loads(self.description_json_array)

    def __str__(self):
        return 'Settings instance'


class Block(models.Model):
    class Meta:
        verbose_name = 'block'
        verbose_name_plural = 'blocks'
        ordering = ['order_id']

    description = models.CharField(verbose_name='description', max_length=255, blank=True)
    order_id = models.IntegerField(verbose_name='order-id')

    def __str__(self):
        return f"Block #{self.order_id}"


class Row(models.Model):
    class Meta:
        verbose_name = 'row'
        verbose_name_plural = 'rows'
        ordering = ['order_id']

    block = models.ForeignKey(
        verbose_name='block',
        to=Block,
        on_delete=models.SET_NULL,
        related_name='rows',
        related_query_name='row',
        null=True
    )
    order_id = models.IntegerField(verbose_name='order-id')

    def __str__(self):
        if self.block:
            return f"Row #{self.order_id} of block #{self.block.order_id}"
        else:
            return f"Row #{self.order_id} (no block)"


class Contact(models.Model):
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['order_id']

    title = models.CharField(verbose_name='title', max_length=255)
    url = models.TextField(verbose_name='url')

    icon = models.ImageField(verbose_name='icon')
    background_color = models.TextField(verbose_name='background-color', max_length=255, default='midnightblue')
    foreground_color = models.TextField(verbose_name='foreground-color', max_length=255, default='lightcyan')

    row = models.ForeignKey(
        verbose_name='row',
        to=Row,
        on_delete=models.SET_NULL,
        related_name='contacts',
        related_query_name='contact',
        null=True
    )
    order_id = models.IntegerField(verbose_name='order_id')

    def __str__(self):
        return self.title

    def width(self):
        return 100 / len(self.row.contacts.all())
