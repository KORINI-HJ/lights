# Generated by Django 3.0.3 on 2020-06-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200614_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='images',
            field=models.ImageField(default='footprint.gif', upload_to='%Y/%m/%d/%H/%m'),
        ),
    ]
