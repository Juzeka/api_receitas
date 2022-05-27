# Generated by Django 4.0.4 on 2022-05-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
        ),
    ]
