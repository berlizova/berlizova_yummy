# Generated by Django 5.0.6 on 2024-05-09 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='gallery/')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RestaurantStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff_photo/')),
                ('bio', models.TextField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Restaurant Staff',
                'verbose_name_plural': 'Restaurant Staff',
            },
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ['sort'], 'verbose_name': 'Dish category', 'verbose_name_plural': 'Dish categories'},
        ),
        migrations.AddField(
            model_name='dishcategory',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
                ('sort', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dishes/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main.dishcategory')),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
                'ordering': ['sort'],
            },
        ),
    ]