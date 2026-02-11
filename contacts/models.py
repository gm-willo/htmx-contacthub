from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = (
        models.EmailField()
    )  # this can't be unique 'cause two different users can create a contact with the same email
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contacts"  # user.contacts.all()
    )

    class Meta:
        unique_together = (
            "user",
            "email",
        )  # it is used to prevent a user to create two contacts with the same email

    def __str__(self):
        return f"{self.name} <{self.email}>"
