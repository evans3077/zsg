from django.db import migrations


def normalize_hall_room_names(apps, schema_editor):
    ConferenceRoom = apps.get_model("conferences", "ConferenceRoom")

    updates = [
        ("bamboo-meeting-room", "Bamboo Conference Hall"),
        ("cactus-meeting-room", "Cactus Conference Hall"),
    ]

    for slug, name in updates:
        ConferenceRoom.objects.filter(slug=slug).update(
            name=name,
            room_type="hall",
        )


def reverse_normalize_hall_room_names(apps, schema_editor):
    ConferenceRoom = apps.get_model("conferences", "ConferenceRoom")

    reversals = [
        ("bamboo-meeting-room", "Bamboo Meeting Room"),
        ("cactus-meeting-room", "Cactus Meeting Room"),
    ]

    for slug, name in reversals:
        ConferenceRoom.objects.filter(slug=slug).update(
            name=name,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0002_remove_training_category_type_choice"),
    ]

    operations = [
        migrations.RunPython(
            normalize_hall_room_names,
            reverse_normalize_hall_room_names,
        ),
    ]
