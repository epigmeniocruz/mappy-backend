# Generated by Django 4.2.6 on 2023-10-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='X',
            field=models.DecimalField(decimal_places=14, max_digits=14),
        ),
        migrations.AlterField(
            model_name='fish',
            name='Y',
            field=models.DecimalField(decimal_places=14, max_digits=14),
        ),
        migrations.AlterField(
            model_name='fish',
            name='Z',
            field=models.DecimalField(decimal_places=14, max_digits=14),
        ),
    ]
