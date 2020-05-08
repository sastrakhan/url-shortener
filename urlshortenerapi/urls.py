# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'urls', views.URLViewSet)
router.register(r'urlvisits', views.URLVisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bit/<slug:url_slug>/', views.show_url_stats),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]