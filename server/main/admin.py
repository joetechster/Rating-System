from django.contrib import admin
from .models import CustomUser, Porter

admin.site.register(Porter)

# class GradeInline(admin.TabularInline):
#   verbose_name_plural = "Lecturers You graded"
#   model = Grade
#   fk_name = 'student'
#   extra = 0
  
#   def has_add_permission(self, request, obj):
#     return obj.type == "student"

# class GradedInline(admin.TabularInline):
#   verbose_name_plural = "Students who graded you"
#   model = Grade
#   fk_name = 'lecturer'
#   # readonly_fields = ('student', 'grade')
#   extra = 0
  
#   def has_add_permission(self, request, obj):
#     return False
#   def has_change_permission(self, request, obj):
#     return False
#   def has_delete_permission(self, request, obj):
#     return False
    
    
    
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'passport')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password', 'username', 'passport', 'type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # Password field should be hidden for security reasons
    readonly_fields = ('password',)
