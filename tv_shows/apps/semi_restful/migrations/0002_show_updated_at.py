# Generated by Django 2.2.3 on 2019-08-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
