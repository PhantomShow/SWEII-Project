# Generated by Django 4.1.1 on 2022-11-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Scout'), (1, 'Athlete')], null=True),
        ),
    ]
