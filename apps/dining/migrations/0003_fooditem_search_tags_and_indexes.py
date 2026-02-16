from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dining", "0002_alter_fooditem_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="fooditem",
            name="search_tags",
            field=models.CharField(
                blank=True,
                help_text="Comma-separated tags for menu search (e.g. vegan, spicy, breakfast)",
                max_length=255,
            ),
        ),
        migrations.AddIndex(
            model_name="fooditem",
            index=models.Index(fields=["is_active", "display_order"], name="dining_food_active_idx"),
        ),
        migrations.AddIndex(
            model_name="fooditem",
            index=models.Index(fields=["name"], name="dining_food_name_idx"),
        ),
        migrations.AddIndex(
            model_name="fooditem",
            index=models.Index(fields=["search_tags"], name="dining_food_tags_idx"),
        ),
    ]
