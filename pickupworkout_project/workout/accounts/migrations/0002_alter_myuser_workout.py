# Generated by Django 3.2 on 2021-06-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='workout',
            field=models.CharField(max_length=255),
        ),
    ]
