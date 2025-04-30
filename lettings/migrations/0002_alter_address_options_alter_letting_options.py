from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Addresses"},
        ),
        migrations.AlterModelOptions(
            name="letting",
            options={"verbose_name_plural": "Lettings"},
        ),
    ]
