# Generated by Django 2.1.2 on 2018-10-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='FotosClientes'),
        ),
    ]
