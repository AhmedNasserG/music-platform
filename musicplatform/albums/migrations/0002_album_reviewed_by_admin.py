# Generated by Django 4.1.2 on 2022-10-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='reviewed_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
