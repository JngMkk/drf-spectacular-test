from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(_("id"), primary_key=True)
    email = models.EmailField(_("이메일"), unique=True, db_index=True)
    created_at = models.DateTimeField(_("생성일"), auto_now_add=True)
    is_admin = models.BooleanField(_("관리자"), default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"
