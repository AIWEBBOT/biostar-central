# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_badges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='domain',
            field=models.CharField(default='www', unique=True, max_length=50, db_index=True),
            preserve_default=True,
        ),
    ]
