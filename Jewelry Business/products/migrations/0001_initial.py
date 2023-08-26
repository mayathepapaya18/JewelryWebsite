# Generated by Django 4.2.3 on 2023-07-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('jewelrytype', models.CharField(choices=[('Necklace', 'Necklace'), ('Bracelet', 'Bracelet'), ('Ring', 'Ring'), ('Earring', 'Earring'), ('Anklet', 'Anklet')], default='necklace', max_length=50)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
    ]
