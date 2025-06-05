from rest_framework import viewsets, permissions
from .models import Career, Comment
from .serializers import CareerModelSerializer, CommentSerializer




class CareerModelViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerModelSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(author=user)
        else:
            raise serializer.ValidationError("User must be authenticated to create a comment.")