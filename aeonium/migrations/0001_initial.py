# Generated by Django 4.1.4 on 2022-12-20 02:18

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', mdeditor.fields.MDTextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
