# Generated by Django 4.1.2 on 2022-10-09 16:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='New Album', max_length=150)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('release_datetime', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
