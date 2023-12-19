from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from service.auth import CustomToken
router = DefaultRouter()

router.register('location-api', views.getLocations, basename="location")
router.register('location', views.Location, basename='go-location')
router.register('readonly-locaton-api',views.ReadOnlyLocation, basename="readonly_api")
router.register('basic-permission',views.myBasicPermission, basename='my-premission')
router.register('session-auth', views.mySessionAuthenticationApi, basename='session_auth')
# Custom Permissions
router.register('custom-permission',views.myCustomPermissionApi, basename='custom_permission')

router.register('token-auth', views.myTokenAuth, basename='token_auth')

urlpatterns = [
    
    path('',views.getHome,name='service'),
    path('api/',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('get-token/',obtain_auth_token),

    # Custom auth token
    path('get-token/',CustomToken.as_view() ),
]
