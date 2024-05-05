from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ads.apps import AdsConfig
from ads.views import AdViewSet, ReviewViewSet


app_name = AdsConfig.name

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'ads/(?P<ad_pk>\d+)/comments', ReviewViewSet, basename='reviews')

urlpatterns = [path("", include(router.urls))]
