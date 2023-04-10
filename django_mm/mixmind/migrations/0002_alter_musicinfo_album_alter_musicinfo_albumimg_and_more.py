# Generated by Django 4.1.7 on 2023-04-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixmind', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicinfo',
            name='album',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='albumImg',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='arranger',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='artist',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='composer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='genre',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='lyricist',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='lyrics',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='releasedDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musicinfo',
            name='youtudeId',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
