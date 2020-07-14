
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  \
                                       PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, gender, password=None,
                    **extra_fields):
        """ creates and saves a new user"""
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ custom user model"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    MALE = 0
    FEMALE = 1
    OTHER = 2
    gender_choices = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.IntegerField(choices=gender_choices, default=MALE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
