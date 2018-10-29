# Generated by Django 2.1.2 on 2018-10-28 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Quantidade', models.IntegerField(default=0)),
                ('Valor', models.FloatField()),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Produto.Categoria')),
            ],
        ),
    ]
