# Generated by Django 4.0.5 on 2022-08-04 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0004_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]