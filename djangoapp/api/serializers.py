from rest_framework import serializers
from api.models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        # fields = ('employeeName', 'employeeID')
        fields = '__all__'