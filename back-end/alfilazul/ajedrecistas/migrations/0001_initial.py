# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajedrecista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField(default=0)),
                ('ranking_local', models.IntegerField(default=0)),
                ('sexo', models.CharField(max_length=1)),
                ('escuela', models.CharField(max_length=150)),
                ('club', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=75)),
                ('bird_date', models.DateTimeField(verbose_name=b'Bird Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
