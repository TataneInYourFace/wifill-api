from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        # Ensure that a username is set
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        mail = self.normalize_email(email)
        user = self.model(
            email=mail,
            username=mail,
            firstname=kwargs.get('firstname', None),
            lastname=kwargs.get('lastname', None),
        )
<<<<<<< HEAD:app/models.py

        user.set_password(password)
        user.save()

=======
        user.set_password(password)
        user.save()
>>>>>>> 83176c9214ae10b3931fa2a7f4fd91e9403120a0:app/models/user_model.py
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, kwargs)
<<<<<<< HEAD:app/models.py

        user.is_admin = True
        user.save()

        return user
=======

        user.is_admin = True
        user.save()

        return user

>>>>>>> 83176c9214ae10b3931fa2a7f4fd91e9403120a0:app/models/user_model.py

class User(AbstractBaseUser):

<<<<<<< HEAD:app/models.py
class User(AbstractBaseUser):
=======
>>>>>>> 83176c9214ae10b3931fa2a7f4fd91e9403120a0:app/models/user_model.py
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)

    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
