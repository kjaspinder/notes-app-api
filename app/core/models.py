
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  \
                                       PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, gender, password=None,
                    **extra_fields):
        """ creates and saves a new user"""
        if not email:
            raise ValueError('Must provide Email Address')
        if not first_name:
            raise ValueError('Must provide first name')
        if not last_name:
            raise ValueError('Must provide last name')
        if not password:
            raise ValueError('Must provide password')

        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, gender,
                         password=None):
        """ creates and saves superuser"""
        user = self.create_user(email, first_name, last_name, gender,
                                password)
        user.is_staff = True
        user.is_superuser = True
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
