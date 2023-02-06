from django.db import models
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length = 250)
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(_('password'), max_length=300)
    is_active  = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_admin = models.BooleanField(_('admin'), default= False)
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email


# class Landlord(models.Model):
#     Fullname = models.CharField(max_length=100,null=True,blank=True)
#     Email = models.EmailField(max_length=100,unique=True,null= True)
#     user = models.OneToOneField(to=User,on_delete=models.CASCADE)
#     phone_no = PhoneNumberField()

#     def __str__(self):
#        return self.user, self.Fullname

# class Tenant(models.Model):
#     Fullname = models.CharField(max_length=100,null=True,blank=True)
#     Email = models.EmailField(max_length=100,unique=True,null= True)
#     user = models.OneToOneField(to=User,on_delete=models.CASCADE)
#     phone_no = PhoneNumberField()

#     def __str__(self):
#        return self.user, self.Fullname