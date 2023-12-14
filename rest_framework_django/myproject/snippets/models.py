from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
print(LEXERS)


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(
        "MyUser", related_name="snippets", on_delete=models.CASCADE
    )
    highlighted = models.TextField()

    class Meta:
        ordering = ["created"]

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager


class Category(models.Model):
    # id= models.IntegerField(null=True, blank=True)
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    class Meta:
        ordering=["title"];



    
class MyUser(AbstractUser):
    pass
    # last_login = None
    # is_staff = None
    # is_superuser = None
    # email = models.EmailField(unique=True, default="abc@example.com")
    # last_login = models.DateTimeField(auto_now_add=True)
    # is_staff = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=True)
    # password = models.CharField(max_length=100)
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = (
    #     []
    # )  # The 'USERNAME_FIELD' is currently set to 'email', you should remove 'email' from the 'REQUIRED_FIELDS'.

    # # Add this line to avoid clashes with groups
    # # groups = models.ManyToManyField("auth.Group", related_name="myuser_set", blank=True)

    # # # Add this line to avoid clashes with user_permissions
    # # user_permissions = models.ManyToManyField(
    # #     "auth.Permission", related_name="myuser_set", blank=True
    # # )

    # def create_user(self, email, password=None):
    #     """
    #     Creates and saves a User with the given email, date of
    #     birth and password.
    #     """
    #     if not email:
    #         raise ValueError("Users must have an email address")

    #     user = self.model(
    #         email=self.normalize_email(email),
    #     )

    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_superuser(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)
    #     # Ensure that 'username' is set to 'email'
    #     extra_fields.setdefault("username", email)

    #     return self.create_user(email, password, **extra_fields)
