from owner.models import Owner
from rest_framework import viewsets, permissions
from owner.serializers import OwnerSerializers

#Owner  Viewsets
# class OwnerViewset(viewsets.ModelViewSet):
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = OwnerSerializers
#     def get_queryset(self): #to get only authenticated user
#         return self.request.user.owner.all()
#
#     def perform_create(self, serializer): #save the owners owner when we create it
#         serializer.save(owner=self.request.user)

class OwnerViewset(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OwnerSerializers

