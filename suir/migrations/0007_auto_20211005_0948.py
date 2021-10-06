# Generated by Django 3.1.7 on 2021-10-05 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suir', '0006_auto_20211004_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicado',
            field=models.DateField(blank=True, help_text='Fecha de publicación', null=True, verbose_name='Fecha publicado'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
