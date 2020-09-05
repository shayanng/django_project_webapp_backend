from django.urls import path, include
from . import views
from .views import BookViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("books", BookViewSet)


urlpatterns = [
    # path('first', views.first),
    path('', include(router.urls))
    # path('another', Another.as_view()),
]
