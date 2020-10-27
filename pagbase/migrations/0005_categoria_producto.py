# Generated by Django 3.1.2 on 2020-10-27 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pagbase', '0004_auto_20201027_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='fotos')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.PositiveIntegerField()),
                ('peso', models.PositiveIntegerField()),
                ('dimension', models.PositiveIntegerField()),
                ('detalle', models.TextField(max_length=300)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagbase.categoria')),
            ],
        ),
    ]
