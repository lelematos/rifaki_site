# Generated by Django 3.0.5 on 2020-05-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_categoria_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='preco',
            field=models.DecimalField(decimal_places=2, default='00.00', error_messages={'invalid': 'Troque a vírgula por ponto!'}, max_digits=6),
        ),
    ]
