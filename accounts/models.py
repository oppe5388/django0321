from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    #last_nameを使うために
    def __str__(self):
        return str(self.last_name)
    # pass
