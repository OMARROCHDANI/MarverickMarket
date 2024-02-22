from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # this perms_map is found in DjangoModelPermissions definition
    # here basically we overriden DjangoModelPermissions perms_map
    # Get, because it was empty, thats why the get method is not 
    # handeled by DjangoModelPermissions (go to views and see ProductDetailAPIView 
    # for more)
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
