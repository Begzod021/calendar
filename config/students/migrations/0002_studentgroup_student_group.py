# Generated by Django 4.0.5 on 2022-06-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='student_group',
            field=models.IntegerField(null=True),
        ),
    ]