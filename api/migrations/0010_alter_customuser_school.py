# Generated by Django 4.1.1 on 2022-11-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_customuser_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='school',
            field=models.CharField(blank=True, choices=[('Georgia Institute of Technology', 'Georgia Institute of Technology'), ('Florida International University', 'Florida International University'), ('Yale', 'Yale'), ('University of Pittsburgh', 'University of Pittsburgh'), ('Emory University', 'Emory University')], max_length=128),
        ),
    ]
