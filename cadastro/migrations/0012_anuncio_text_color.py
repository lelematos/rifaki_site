# Generated by Django 3.0.5 on 2020-05-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_auto_20200521_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='text_color',
            field=models.CharField(choices=[('black', 'Preto'), ('white', 'Branco'), ('grey', 'Cinza')], default='black', max_length=10),
        ),
    ]
