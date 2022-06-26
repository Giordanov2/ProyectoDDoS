# Generated by Django 4.0.5 on 2022-06-20 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analisis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_source', models.CharField(max_length=15)),
                ('ip_dest', models.CharField(max_length=15)),
                ('port_source', models.IntegerField(null=True)),
                ('port_dest', models.IntegerField(null=True)),
                ('protocol', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='analisis',
            name='cantidad_paquetes_analizados',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='analisis',
            name='cantidad_paquetes_malignos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='analisis',
            name='cantidad_paquetes_normales',
            field=models.IntegerField(null=True),
        ),
    ]
