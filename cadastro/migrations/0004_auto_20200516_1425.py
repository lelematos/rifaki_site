# Generated by Django 3.0.5 on 2020-05-16 17:25

import cadastro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20200516_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagem1',
            field=models.ImageField(upload_to=cadastro.models.user_directory_path),
        ),
    ]
