# Generated by Django 3.2.9 on 2022-03-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, choices=[('Music', 'Music'), ('Fashion', 'Fashion'), ('Car', 'Car'), ('Travel', 'Travel'), ('Technology', 'Technology'), ('Movies', 'Movies'), ('History', 'History'), ('Lifestyle', 'Lifestyle'), ('Overall', 'Overall')], default='OV', help_text='Blogpost category', max_length=20),
        ),
    ]