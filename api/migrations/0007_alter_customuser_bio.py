# Generated by Django 4.1.1 on 2022-11-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_customuser_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, default='No biography', null=True),
        ),
    ]