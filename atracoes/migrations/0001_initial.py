# Generated by Django 2.1.5 on 2019-01-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(max_length=300)),
                ('horario_func', models.TextField(max_length=10)),
                ('idade_minima', models.IntegerField()),
            ],
        ),
    ]
