# Generated by Django 3.1 on 2020-08-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
