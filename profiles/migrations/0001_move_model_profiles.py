from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
from django.db.migrations.operations.special import SeparateDatabaseAndState


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Profile",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("favorite_city", models.CharField(max_length=64, blank=True)),
                        (
                            "user",
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                    ],
                    options={
                        "db_table": "oc_lettings_site_profile",
                    },
                ),
            ],
            database_operations=[],
        )
    ]
