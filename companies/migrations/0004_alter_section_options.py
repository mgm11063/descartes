# Generated by Django 4.0.4 on 2022-04-13 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_company_options_alter_section_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '구역 '},
        ),
    ]
