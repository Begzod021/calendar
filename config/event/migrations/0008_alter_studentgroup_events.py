# Generated by Django 4.0.5 on 2022-06-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_remove_event_student_studentgroup_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='events',
            field=models.ManyToManyField(to='event.event'),
        ),
    ]
