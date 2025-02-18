# Generated by Django 3.0.5 on 2020-05-13 18:42

import cadastro.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador_anuncio', models.IntegerField()),
                ('titulo_anuncio', models.CharField(max_length=100)),
                ('ano_fabricacao', models.DateField()),
                ('descricao_breve', models.TextField(max_length=400)),
                ('descricao_completa', models.TextField(max_length=2000)),
                ('imagem1', models.ImageField(blank=True, null=True,
                                              upload_to=cadastro.models.user_directory_path)),
                ('imagem2', models.ImageField(blank=True, null=True,
                                              upload_to=cadastro.models.user_directory_path)),
                ('imagem3', models.ImageField(blank=True, null=True,
                                              upload_to=cadastro.models.user_directory_path)),
                ('imagem4', models.ImageField(blank=True, null=True,
                                              upload_to=cadastro.models.user_directory_path)),
                ('imagem5', models.ImageField(blank=True, null=True,
                                              upload_to=cadastro.models.user_directory_path)),
                ('mem_categorias', models.CharField(max_length=1000, null=True)),
                ('data_publi', models.DateTimeField(
                    verbose_name='data publicação')),
                ('anunciante', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
