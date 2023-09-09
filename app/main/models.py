from django.db import models


class Page(models.Model):
    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    is_homepage = models.BooleanField(verbose_name='is-homepage', default=False)
    slug = models.SlugField(verbose_name='slug', max_length=255, unique=True)

    background_image = models.ImageField(verbose_name='background-image')
    icon = models.ImageField(verbose_name='icon')

    title = models.TextField(verbose_name='title', max_length=255, blank=True)
    name = models.TextField(verbose_name='name', max_length=255, blank=True)
    description = models.TextField(verbose_name='description', blank=True)

    def description_array(self):
        return self.description.split('\n')

    def __str__(self):
        return f'{self.slug} (homepage)' if self.is_homepage else f'{self.slug}'


class Block(models.Model):
    class Meta:
        verbose_name = 'block'
        verbose_name_plural = 'blocks'
        ordering = ['order_id']

    description = models.CharField(verbose_name='description', max_length=255, blank=True)

    page = models.ForeignKey(
        verbose_name='page',
        to=Page,
        on_delete=models.SET_NULL,
        related_name='blocks',
        related_query_name='block',
        null=True,
        blank=True
    )
    order_id = models.IntegerField(verbose_name='order-id')

    def __str__(self):
        if self.page:
            return f"Block #{self.order_id} of {self.page}"
        return f"Block #{self.order_id} (no page)"


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
        null=True,
        blank=True
    )
    order_id = models.IntegerField(verbose_name='order-id')

    def length(self):
        return len(self.texts.all()) + len(self.links.all())

    def items(self):
        data = list(self.links.all()) + list(self.texts.all())
        data.sort(key=lambda item: item.order_id)
        return data

    def __str__(self):
        if self.block:
            return f"Row #{self.order_id} of {self.block}"
        else:
            return f"Row #{self.order_id} (no block)"


class Item(models.Model):
    class Meta:
        abstract = True
        ordering = ['order_id']

    title = models.CharField(verbose_name='title', max_length=255)

    icon = models.ImageField(verbose_name='icon', null=True, blank=True)

    row = models.ForeignKey(
        verbose_name='row',
        to=Row,
        on_delete=models.SET_NULL,
        related_name='%(class)ss',
        related_query_name='%(class)s',
        null=True,
        blank=True
    )
    order_id = models.IntegerField(verbose_name='order_id')

    def width(self):
        return 100 / self.row.length()

    def type(self):
        return self.__class__.__name__


class Text(Item):
    class Meta:
        verbose_name = 'text'
        verbose_name_plural = 'texts'

    description = models.TextField(verbose_name='description', null=True, blank=True)

    def description_array(self):
        return self.description.split('\n')

    def __str__(self):
        return self.title


class Link(Item):
    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'

    url = models.TextField(verbose_name='url')

    background_color = models.TextField(verbose_name='background-color', max_length=255, default='midnightblue')
    foreground_color = models.TextField(verbose_name='foreground-color', max_length=255, default='lightcyan')

    def __str__(self):
        return self.title
