# Generated by Django 3.1.6 on 2021-02-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BS_APP', '0004_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]