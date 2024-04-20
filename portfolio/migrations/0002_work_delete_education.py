# Generated by Django 5.0.4 on 2024-04-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Education', 'Education'), ('Work', 'Work')], max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=200)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Education',
        ),
    ]