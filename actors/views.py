from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateLisView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
