from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
    path('', api_root, name='api-root'),
]
