# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from pootle.core.delegate import formats


def initialize_formats(apps, schema_editor):
    formats.get().initialize()


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(initialize_formats),
    ]
