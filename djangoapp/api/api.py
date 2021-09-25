from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import * 

class UserList(APIView):
    def get(self, request):
        model = Users.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get_user(self, employeeID):
        try:
            model = Users.objects.get(id=employeeID)
            return model
        except Users.DoesNotExist:
            return

    def get(self, request, employeeID):
        if not self.get_user(employeeID):
            return Response(f'User with ID: {employeeID} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(employeeID))
        return Response(serializer.data)

    def put(self, request, employeeID):
        if not self.get_user(employeeID):
            return Response(f'User with ID: {employeeID} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(employeeID), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employeeID):
        if not self.get_user(employeeID):
            return Response(f'User with ID: {employeeID} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(employeeID)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)