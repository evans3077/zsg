from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingrequest",
            name="end_datetime",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="bookingrequest",
            name="start_datetime",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
