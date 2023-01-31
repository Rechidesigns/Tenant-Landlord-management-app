from django.db import models
# from accounts.models import User,Profile



class Apartment(models.Model):
    # user = models.ForeignKey(to=Profile, on_delete=CASCADE)
    owner_Name = models.CharField(max_length=100,null=True)
    owner_pic = models.ImageField(upload_to='Housepic', null=True, blank=True)
    house_address  =models.TextField(null=False)
    building_img1 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    boom_img1 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    room_img2 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    room_img3 = models.ImageField(upload_to='Housepic', null=True, blank=True)
    landmark = models.TextField(null=False)
    house_type = models.CharField(max_length=100,null = False,default="2BD/3BD/1BD/ROOMANDPALOOR/ROOMSELF")
    house_description = models.TextField(null = False,default="Write something About how good and what are the facilities your renters will get there like electricity/Water etc")
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=200, null=False)
    phone_no = models.IntegerField(null=False)
    Price = models.IntegerField(null = False, default= 1000)
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Owner_Name


STATUS_CHOICES =(
    ('SINGLE', 'single'),
    ('MARRIED', 'FAMILY OF ONE'),
    ('MARRIED', 'FAMILY OF TWO'),
    ('MARRIED', 'FAMILY OF THREE'),
    ('MARRIED', 'FAMILY OF FOUR'),
    ('MARRIED', 'FAMILY OF FIVE'),
    ('MARRIED', 'FAMILY OF SIX'),
)

class Tenant(models.Model):
    # user = models.ForeignKey(to=Profile, on_delete=CASCADE)
    tenant_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='tenant_picture', blank=True, null=True)
    family_size = models.CharField(max_length= 200, choices = STATUS_CHOICES, default= 'single')
    phone_no = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=200, null=False)
    landlord_name = models.CharField(max_length=100, null=True, blank=True)
    landlords_phone_no = models.IntegerField(null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.tenant_Name
