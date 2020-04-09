from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.contrib.auth.models import User

from .serializers import UserSerializer, DetailSerializer
from .permissions import IsOwnerOrAdminOrReadOnly


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DetailSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

        
