from django.db.migrations.operations.special import SeparateDatabaseAndState
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("oc_lettings_site", "0001_initial"),  # ou la dernière migration précédente
    ]

    operations = [
        SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(name="Address"),
                migrations.DeleteModel(name="Letting"),
                migrations.DeleteModel(name="Profile"),
            ],
            database_operations=[],  # ✅ aucune suppression réelle en base
        )
    ]
