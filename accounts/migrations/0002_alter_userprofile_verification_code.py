# Generated by Django 5.1.3 on 2024-11-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='verification_code',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Код верификации'),
        ),
    ]