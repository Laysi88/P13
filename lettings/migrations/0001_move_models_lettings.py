from django.db import migrations, models
import django.db.models.deletion
import django.core.validators
from django.db.migrations.operations.special import SeparateDatabaseAndState


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Address",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                primary_key=True,
                                serialize=False,
                                auto_created=True,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "number",
                            models.PositiveIntegerField(
                                validators=[django.core.validators.MaxValueValidator(9999)]
                            ),
                        ),
                        ("street", models.CharField(max_length=64)),
                        ("city", models.CharField(max_length=64)),
                        (
                            "state",
                            models.CharField(
                                max_length=2,
                                validators=[django.core.validators.MinLengthValidator(2)],
                            ),
                        ),
                        (
                            "zip_code",
                            models.PositiveIntegerField(
                                validators=[django.core.validators.MaxValueValidator(99999)]
                            ),
                        ),
                        (
                            "country_iso_code",
                            models.CharField(
                                max_length=3,
                                validators=[django.core.validators.MinLengthValidator(3)],
                            ),
                        ),
                    ],
                    options={
                        "db_table": "oc_lettings_site_address",
                    },
                ),
                migrations.CreateModel(
                    name="Letting",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                primary_key=True,
                                serialize=False,
                                auto_created=True,
                                verbose_name="ID",
                            ),
                        ),
                        ("title", models.CharField(max_length=256)),
                        (
                            "address",
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE, to="lettings.Address"
                            ),
                        ),
                    ],
                    options={
                        "db_table": "oc_lettings_site_letting",
                    },
                ),
            ],
            database_operations=[],
        )
    ]
