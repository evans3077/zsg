from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_homepagesettings_hero_subtitle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepagesettings",
            name="address",
            field=models.TextField(default="Kithini, Machakos, 55 km from Nairobi GPO"),
        ),
    ]
