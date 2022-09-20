from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _

class CustomBaseUserManager(BaseUserManager):
    def create_user(self, email, name, type, password=None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, type=type)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, type, password=None):
        """
        this method is used for creating super user with the command below:
        python manage.py createsuperuser
        """
        user = self.create_user(email=email, name=name, type=type, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Model for the User. We're creating a Custom User model with our own required fields
        
    as we are creating our own custom user model, we have to add this to settings (AUTH_USER_MODEL), in order to use the custom model for authentication.
    """

    class Types(models.TextChoices):
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"

    #Type of user
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, null=True, blank=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomBaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'type'] #email is required by default

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email
