from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name_plural": "Profiles"},
        ),
    ]
