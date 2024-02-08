from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer  
from .models import Location, ParentLocations
from .serializer import LocationSerializer, ParentLocationSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .custompermissions import myBasePermission
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class MyThrotal(viewsets.ModelViewSet):
    queryset = ParentLocations.objects.all()
    serializer_class = ParentLocationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class MyLocationViewModelSet(viewsets.ModelViewSet):
    queryset= ParentLocations.objects.all()
    serializer_class = ParentLocationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class myLocation(viewsets.ViewSet):
    def list(self,request):
        lcData = ParentLocations.objects.all()
        slrdata = ParentLocationSerializer(lcData, many=True)
        return Response(slrdata.data)

def getApi(request):
    return  HttpResponse(0)

class myTokenAuth(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [myBasePermission]

# custom permissions
class myCustomPermissionApi(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [myBasePermission]

class mySessionAuthenticationApi(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]


class myBasicPermission(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


## read only model view sets
class ReadOnlyLocation(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

## model view set
class Location(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class getLocations(viewsets.ViewSet):
    def list(self,request):
        locationData = Location.objects.all()
        srlData = LocationSerializer(locationData, many=True)
        return Response(srlData.data)
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            locationData = Location.objects.get(id=id)
            srlData = LocationSerializer(locationData)
            return Response(srlData.data)

    def create(self, request):
        return Response(10)

def getHome(request):
    if request.method == "GET":
        # locationData = Location.objects.get(id=1)    
        locationData = Location.objects.all()
        srlData = LocationSerializer(locationData, many=True)
        jsonResp = JSONRenderer().render( srlData.data )     
        return HttpResponse( jsonResp, content_type="application/json" )
    jsonResp = {'msg': 'please user authorized request method', 'status': 404}
    return HttpResponse(jsonResp, content_type="application/json")