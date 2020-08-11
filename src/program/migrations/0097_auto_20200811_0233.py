# Generated by Django 3.1 on 2020-08-11 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0096_auto_20200810_2034"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventfeedback",
            name="approved",
            field=models.BooleanField(
                help_text="Approve feedback? It will not be visible to the Event owner before it is approved.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="eventslot",
            name="autoscheduled",
            field=models.BooleanField(
                default=None,
                help_text="True if the Event was scheduled by the AutoScheduler, False if it was scheduled manually, None if there is nothing scheduled in this EventSlot.",
                null=True,
            ),
        ),
    ]
