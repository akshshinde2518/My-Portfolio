# Generated by Django 5.1.3 on 2024-11-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_about_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]