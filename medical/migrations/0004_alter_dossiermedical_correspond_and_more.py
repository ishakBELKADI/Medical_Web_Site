# Generated by Django 5.0.1 on 2024-01-28 00:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0003_alter_rdv_estchargéinf_alter_rdv_estchargémed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiermedical',
            name='correspond',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medical.patient'),
        ),
        migrations.AlterField(
            model_name='dossiermedical',
            name='estlier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medical.medecin'),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='heureRdv',
            field=models.TimeField(default=datetime.time(0, 58, 4, 705142)),
        ),
    ]
