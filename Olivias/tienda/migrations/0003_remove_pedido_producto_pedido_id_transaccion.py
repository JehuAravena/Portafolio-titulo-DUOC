# Generated by Django 4.1.1 on 2022-09-29 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_transaccion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]