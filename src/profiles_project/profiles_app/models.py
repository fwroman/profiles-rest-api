from django.db import models

# FOR AUTHENTICATION:
from django.contrib.auth.models import AbstractBaseUser
# PERMISSIONS FOR SPECIFIC USERS TO LET THEM TO DO SOMETHING:
from django.contrib.auth.models import PermissionsMixin

#
from django.contrib.auth.models import BaseUserManager
# Create your models here.

# MANAGER CLASS TO HANDLE ALL MODELS:


class UserProfileManager(BaseUserManager):
    """
    HELPS DJANGO WORK WITH UR CUSTOM USER MODEL.
    """

    def create_user(self, email, name, password=None):
        """
        CREATES A NEW USER PROFILE OBJECTS
        """

        if not email:
            raise ValueError('Users must have an email address.')

        # CONVERTS EVERY EMAIL CHARACTER TO LOWERCASE:
        # REF: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email
        email = self.normalize_email(email)
        #

        user = self.model(email=email, name=name)

        # NEXT FUNCTIONS WILL ENCRYPT PASSWORD FOR US, RETURNING A HASH TO BE
        # STORED IN OUR DATABASE:
        user.set_password(password)
        #
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        CREATES AND SAVES A NEW SUPERUSER WITH GIVEN DETAILS:
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    REPRESENT A "USER PROFILE" INSIDE OUR SYSTEM.
    """

    # DJANGO MODELS REF: https://docs.djangoproject.com/en/1.11/topics/db/models/
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_start = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'  # EMAIL IS REQUIRED BY DEFAULT
    REQUIRED_FIELDS = ['name', ]

    def get_full_name(self):
        """
        USED TO GET A USER'S FULL NAME
        """
        return self.name

    def get_short_name(self):
        """
        USED TO GET A USER'S SHORT NAME
        """
        return self.name

    def __str__(self):
        """
        DJANGO USES THIS WHEN IT NEEDS TO CONVERT THE OBJECT TO A STRING
        """
        return self.email


class ProfileFeedItem(models.Model):
    """
    PROFILE STATUS UPDATE
    """

    user_profile = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        RETURN THE MODEL AS STRING
        """
        return self.status_text
