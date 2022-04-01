# Generated by Django 2.2.12 on 2021-11-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20211127_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='Freq_1',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Frequência 1º Bim'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='Freq_2',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Frequência 2º Bim'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='Freq_3',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Frequência 3º Bim'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='Freq_4',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Frequência 4º Bim'),
        ),
    ]