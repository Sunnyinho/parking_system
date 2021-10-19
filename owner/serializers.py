from rest_framework import serializers
from owner.models import Owner

#Owner Serializers
#Helps to convert files into JSON or XML format

class OwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__' 