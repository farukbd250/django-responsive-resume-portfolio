# Generated by Django 5.0.4 on 2024-04-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='review_client/')),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=75)),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]