# Generated by Django 3.1.7 on 2021-07-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=10)),
            ],
        ),
    ]
