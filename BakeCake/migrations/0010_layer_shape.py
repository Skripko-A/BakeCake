# Generated by Django 5.1 on 2024-08-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0009_rename_berrie_berry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Форма')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=10)),
            ],
        ),
    ]
