from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from accounts.models import User,Profile

STATUS_CHOICES =(
    ('single room', 'Single Room'),
    ('room self contain', 'Room self contain'),
    ('room and palor', 'Room and palor'),
    ('one bedroom flat', 'One bedroom flat'),
    ('two bedroom flat', 'Two beedrooms flat'),
    ('three bedroom flat', 'Three beedrooms flat'),
    ('four bedroom flat', 'Four beedrooms flat'),
    ('five bedroom flat', 'Five beedrooms flat'),
    ('six bedroom flat', 'Six beedrooms flat'),
    ('duplex', 'Duplex'),
    ('appartment', 'Appartment'), 

)

class Apartment(models.Model):
    owner_Name = models.CharField(max_length=100,null=True)
    owner_pic = models.ImageField(upload_to='Housepic', null=True, blank=True)
    house_address  = models.CharField(max_length=200, null=False)
    house_image1 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    house_image2 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    house_image3 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    house_image4 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    landmark = models.CharField(max_length=200, null=False)
    house_type = models.CharField(max_length=200,choices = STATUS_CHOICES, default= 'appartment')
    house_description = models.TextField(null = False,)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=200, null=False)
    phone_no = PhoneNumberField()
    email = models.EmailField(null=True, blank=True)
    Price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.owner_Name


STATUS_CHOICES =(
    ('Single', 'single'),
    ('family size', 'Family of one'),
    ('family size', 'Family of two'),
    ('family size', 'Family of three'),
    ('family size', 'Family of four'),
    ('family size', 'Family of five'),
    ('family size', 'Family of six'),
    ('family size', 'Family of six and above'),
)

class Tenant(models.Model):
    tenant_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='tenant_picture', blank=True, null=True)
    family_size = models.CharField(max_length= 200, choices = STATUS_CHOICES, default= 'single')
    phone_no = PhoneNumberField()
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=200, null=False)
    landlord_name = models.CharField(max_length=100, null=True, blank=True)
    landlords_phone_no = PhoneNumberField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.tenant_name
