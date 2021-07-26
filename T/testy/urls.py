from django.contrib import admin
from django.urls import path, include
from testy.views import  *
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Сериализаторы описывают представление данных.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# Наборы представлений описывают поведение представлений.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Роутеры позволяют быстро и просто сконфигурировать адреса.

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]







