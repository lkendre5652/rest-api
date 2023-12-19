from rest_framework.permissions import BasePermission

class myBasePermission(BasePermission):
    def has_permission(self,request,view):
        if request.method == "GET":
            return True
        elif request.method == "POST":
            return True
        else:
            return False
