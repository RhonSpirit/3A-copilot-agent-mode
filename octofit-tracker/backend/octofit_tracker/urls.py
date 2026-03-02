from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f"http://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
    path('', api_root, name='api-root'),
]
