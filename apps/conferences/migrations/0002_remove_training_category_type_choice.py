from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conferencecategory",
            name="category_type",
            field=models.CharField(
                choices=[
                    ("board", "Board Rooms"),
                    ("meeting", "Meeting Rooms"),
                    ("hall", "Meeting Hall"),
                ],
                max_length=20,
            ),
        ),
    ]
