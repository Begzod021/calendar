# Generated by Django 4.0.5 on 2022-06-30 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_studentgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='event.studentgroup'),
        ),
    ]
