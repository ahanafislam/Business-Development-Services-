# Generated by Django 2.1.7 on 2019-04-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceProvider', '0002_provider_submit_submit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider_submit',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
