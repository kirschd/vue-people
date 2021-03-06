# Generated by Django 2.0.6 on 2018-06-28 13:15

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0021_remove_person_news_opt_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetupEvent',
            fields=[
                ('id', models.CharField(editable=False, max_length=512, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='UTC Date')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='MeetupGroup',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.AddField(
            model_name='meetupevent',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.MeetupGroup'),
        ),
    ]
