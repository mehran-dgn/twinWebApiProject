from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models 

class UserManager(BaseUserManager):
    def create_user(self,username, email, password = None , **extra_fields):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        
        extra_fields.setdefault("is_active", True)
        
        email = self.normalize_email(email)
        user = self.model(
            username = username , 
            email = email , 
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    mobile_phone = models.CharField(max_length=14 ,  null=True , blank=True)

    company_phone = models.CharField(max_length = 14 ,  null=True , blank=True)

    postal_code = models.CharField(max_length=10 , null=True , blank=True)
    address = models.TextField(max_length=255 ,  null=True , blank=True)  

    #dashboard_link = models.URLField(blank=True, null = True)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    date_joined = models.DateTimeField(auto_now_add = True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
    
class UserProjects(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete= models.CASCADE,
        related_name =  'projects'
    )
    project_url = models.URLField(blank = True , null = True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.title
