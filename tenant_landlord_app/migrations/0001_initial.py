# Generated by Django 4.1.5 on 2023-02-06 20:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_Name', models.CharField(max_length=100, null=True)),
                ('owner_pic', models.ImageField(blank=True, null=True, upload_to='Housepic')),
                ('house_address', models.CharField(max_length=200)),
                ('house_image1', models.ImageField(blank=True, null=True, upload_to='Housepic')),
                ('house_image2', models.ImageField(blank=True, null=True, upload_to='Housepic')),
                ('house_image3', models.ImageField(blank=True, null=True, upload_to='Housepic')),
                ('house_image4', models.ImageField(blank=True, null=True, upload_to='Housepic')),
                ('landmark', models.CharField(max_length=200)),
                ('house_type', models.CharField(choices=[('single room', 'Single Room'), ('room self contain', 'Room self contain'), ('room and palor', 'Room and palor'), ('one bedroom flat', 'One bedroom flat'), ('two bedroom flat', 'Two beedrooms flat'), ('three bedroom flat', 'Three beedrooms flat'), ('four bedroom flat', 'Four beedrooms flat'), ('five bedroom flat', 'Five beedrooms flat'), ('six bedroom flat', 'Six beedrooms flat'), ('duplex', 'Duplex'), ('appartment', 'Appartment')], default='appartment', max_length=200)),
                ('house_description', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('available', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='tenant_picture')),
                ('family_size', models.CharField(choices=[('Single', 'single'), ('family size', 'Family of one'), ('family size', 'Family of two'), ('family size', 'Family of three'), ('family size', 'Family of four'), ('family size', 'Family of five'), ('family size', 'Family of six'), ('family size', 'Family of six and above')], default='single', max_length=200)),
                ('house_type', models.CharField(choices=[('Single', 'single'), ('family size', 'Family of one'), ('family size', 'Family of two'), ('family size', 'Family of three'), ('family size', 'Family of four'), ('family size', 'Family of five'), ('family size', 'Family of six'), ('family size', 'Family of six and above')], default='appartment', max_length=200)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('valid_ID', models.ImageField(blank=True, null=True, upload_to='I_D')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('landlord_name', models.CharField(blank=True, max_length=100, null=True)),
                ('landlords_phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
