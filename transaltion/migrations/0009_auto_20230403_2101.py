# Generated by Django 3.2 on 2023-04-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaltion', '0008_auto_20230403_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct_answer_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='correct_answer'),
        ),
        migrations.AddField(
            model_name='questions',
            name='correct_answer_en',
            field=models.CharField(max_length=200, null=True, verbose_name='correct_answer'),
        ),
    ]