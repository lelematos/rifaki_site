# Generated by Django 3.0.5 on 2020-05-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20200516_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='preco',
            field=models.DecimalField(decimal_places=2, default='00,00', error_messages={'invalid': 'Troque a vírgula por ponto!'}, max_digits=6),
        ),
    ]
