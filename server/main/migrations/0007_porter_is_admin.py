# Generated by Django 5.0.6 on 2024-07-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_porter'),
    ]

    operations = [
        migrations.AddField(
            model_name='porter',
            name='is_admin',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
