from rest_framework import permissions

class IsOwnerOrIsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or request.user.is_superuser
      
class IsStudent(permissions.BasePermission): 
  message = "Only students can grade lecturers"
  
  def has_permission(self, request, view):
    return request.user.type == "student"