# Generated by Django 4.1.1 on 2022-09-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('final_grade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('points', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.exam')),
            ],
        ),
    ]
