# Generated by Django 2.0.6 on 2018-11-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20181109_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='semester',
            field=models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII')], default='I', max_length=5),
        ),
    ]
