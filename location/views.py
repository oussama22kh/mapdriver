from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from location.serializer import LocationSerializer
from .models import Location


class location(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            location_instance = serializer.save()
            serialized_data = LocationSerializer(location_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        locations = Location.objects.get(pk=pk)
        serializer = LocationSerializer(locations)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, ):
        l = Location.objects.get(pk=pk)
        serializer = LocationSerializer(l, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
