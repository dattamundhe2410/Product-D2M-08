# Generated by Django 4.1.4 on 2023-05-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_assessment_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='result',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
