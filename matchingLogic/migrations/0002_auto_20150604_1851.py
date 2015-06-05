# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchingLogic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='middle_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
