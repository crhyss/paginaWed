# Generated by Django 3.1.2 on 2020-10-27 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagbase', '0003_producto_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
