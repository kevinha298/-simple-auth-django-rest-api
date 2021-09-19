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
    def get(self, request, employeeID):
        try:
            model = Users.objects.get(id=employeeID)
        except Users.DoesNotExist:
            return Response(f'User with ID: {employeeID} is not found in database.', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(model)
        return Response(serializer.data)

    def put(self, request, employeeID):
        try:
            model = Users.objects.get(id=employeeID)
        except Users.DoesNotExist:
            return Response(f'User with ID: {employeeID} is not found in database.', status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)