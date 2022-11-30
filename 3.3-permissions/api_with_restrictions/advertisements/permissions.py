from rest_framework.permissions import BasePermission


# class IsOwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method == 'GET':
#             return True
#         #если админ разрешено
#         # if (request.user and request.user.is_staff):
#         #     return True
#         return request.user == obj.creator

class IsAdvertisementOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.creator == request.user