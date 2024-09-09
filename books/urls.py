from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import AuthorModelViewSet, CategoryModelViewSet, BookModelViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelViewSet)
router.register(r'categories', CategoryModelViewSet)
router.register(r'books', BookModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
