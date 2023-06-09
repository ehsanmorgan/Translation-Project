# Generated by Django 3.2 on 2023-03-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaltion', '0006_remove_vintage_wine_delete_winery_delete_vintage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={},
        ),
        migrations.AddField(
            model_name='questions',
            name='first_option_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='first_option'),
        ),
        migrations.AddField(
            model_name='questions',
            name='first_option_en',
            field=models.CharField(max_length=200, null=True, verbose_name='first_option'),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_en',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='questions',
            name='second_option_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='second_option'),
        ),
        migrations.AddField(
            model_name='questions',
            name='second_option_en',
            field=models.CharField(max_length=200, null=True, verbose_name='second_option'),
        ),
        migrations.AddField(
            model_name='questions',
            name='third_option_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='third_option'),
        ),
        migrations.AddField(
            model_name='questions',
            name='third_option_en',
            field=models.CharField(max_length=200, null=True, verbose_name='third_option'),
        ),
    ]
