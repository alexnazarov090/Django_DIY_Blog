# Generated by Django 3.2.9 on 2022-01-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blogpost_liked_disliked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='blog/images/blog-default-image.jpg', null=True, upload_to='blog/images'),
        ),
    ]