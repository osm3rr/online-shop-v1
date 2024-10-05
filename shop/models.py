from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name',]),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
        )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(
        upload_to='products', blank=True
        )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name', ]),
            models.Index(fields=['-created', ]),
        ]
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
       return self.name