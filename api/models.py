import datetime
import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, first_name,last_name,phone_number,device_type,device_token, password=None, ):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          first_name=first_name,
          last_name=last_name,
          phone_number=phone_number,
          device_type=device_type,
          device_token=device_token
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200,null=True,blank=True)
  phone_number= models.CharField(max_length=20,null=True,blank=True)
  profile_image= models.ImageField(upload_to=getFileName,null=True,blank=True)
  device_type = models.CharField(max_length=255,null=True,blank=True)
  device_token=models.CharField(default="eQJM6WkmQZ6wTKJGLU74hw:APA91bHkQp4-dw3zSqf9Pn53u4ed7o_XWH0eFou7-ZITVAYaZU2K97kPmt9KUlRtsnDYjqImBaMGVBq67J91jMCpy1jpDKVZYIJc1rVN6jODqNYPwZ0bc-J8DdXjp3LckGsi_BXMHXya",max_length=255)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'phone_number','device_type','device_token']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin




