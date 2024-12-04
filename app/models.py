from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
class UserProfileManager(BaseUserManager):
    def create_user(self,email,fn,ln,password=None):
        if not email:
            raise ValueError('send correct email')
        nemail=self.normalize_email(email)
        uo=self.model(email=nemail,fn=fn,ln=ln)
        uo.set_password(password)
        uo.save
        return uo
    def create_superuser(self,email,fn,ln,password):
        uo=self.create_user(email,fn,ln,password)
        uo.is_staff=True
        uo.is_superuser=True
        uo.save()
class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    fn=models.CharField(max_length=100)
    ln=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True) 
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['fn','ln']   