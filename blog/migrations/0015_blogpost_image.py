# Generated by Django 3.2.9 on 2022-01-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='blog/images/blog-default-image.jpg', null=True, upload_to='blog/images'),
        ),
    ]