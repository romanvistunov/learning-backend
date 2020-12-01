from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    color = ColorField(default='#FF0000')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('system:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    parent = models.ForeignKey(Category, related_name='sub_items', on_delete=models.CASCADE, null=True)
    name = models.CharField('Название', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    color = ColorField(default='#C0C0C0')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def get_absolute_url(self):
        return reverse('system:product_list_by_subcategory', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='cat_items', on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, related_name='sub_items', on_delete=models.CASCADE, null=True)
    name = models.CharField('Название', max_length=200, db_index=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    description = models.TextField('Состав', blank=True)
    size = models.CharField('Размер порции', max_length=200, blank=True)
    image = models.ImageField('Картинка', upload_to='upload', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('system:product_detail', args=[self.id])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name