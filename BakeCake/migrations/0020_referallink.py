# Generated by Django 5.1 on 2024-08-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0019_remove_cake_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('visits', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
