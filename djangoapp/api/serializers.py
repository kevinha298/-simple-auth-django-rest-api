from rest_framework import serializers
from api.models import Users

class UserSerializer(serializers.ModelSerializer):
    employeeID = serializers.CharField(required=False)
    employeeName = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)
    class Meta:
        model = Users
        # fields = ('employeeName', 'employeeID')
        fields = '__all__'