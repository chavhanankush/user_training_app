from django.shortcuts import render
from training_app.models import User,Training,Review,Assignment,Client
from training_app.serializers import UserSerializer,TrainingSerializer,ReviewSerializer,AssignmentSerialzer,ClientSerializer
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class UserViewSets(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        id=pk
        user = User.objects.get(id=pk)
        user.delete()
        return Response({'msg': "User Deleted"}, status=status.HTTP_204_NO_CONTENT)

class TrainingViewSets(viewsets.ViewSet):
    def list(self, request):
        training = Training.objects.all()
        serializer = TrainingSerializer(training, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            training = Training.objects.get(id=pk)
            serializer = TrainingSerializer(training)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Training Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        training = Training.objects.get(id=pk)
        serializer = UserSerializer(training, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Training Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        id=pk
        training = Training.objects.get(id=pk)
        training.delete()
        return Response({'msg': "Training Deleted"}, status=status.HTTP_204_NO_CONTENT)
