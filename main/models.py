from django.db import models
from django.utils.text import slugify


# Create your models here.
# Define a function to generate slug
def generate_slug(name):
    return slugify(name)


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    slug = models.SlugField(max_length=255, default='', blank=True)

    # Override save method to generate slug automatically
    def save(self, *args, **kwargs):
        # If slug is not provided, generate it from name
        if not self.slug:
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dish category'
        verbose_name_plural = 'Dish categories'
        ordering = ['sort']


class RestaurantStaff(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='staff_photo/', blank=True, null=True)
    bio = models.TextField()  # field for staff biography
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant Staff'
        verbose_name_plural = 'Restaurant Staff'


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    sort = models.PositiveSmallIntegerField()

    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ['sort']


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering = ['name']
