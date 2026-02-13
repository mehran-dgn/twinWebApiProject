from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProjects


@admin.register(UserProjects)
class UserProjectsAdmin(admin.ModelAdmin):

    model = UserProjects

    list_display = ("user","project_url","title","description")
    



@admin.register(User)
class UserAdmin(BaseUserAdmin):

    model = User

    list_display = ("username", "email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", 'mobile_phone','company_phone','postal_code','address')}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "first_name",
                "last_name",
                #"dashboard_link",
                'mobile_phone',
                'company_phone',
                'postal_code',
                'address',
                "password1",
                "password2",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)
