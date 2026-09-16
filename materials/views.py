from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsModerator, IsOwner

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name="Moderator").exists():
            return Course.objects.all()

        return Course.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]

        elif self.action in ["retrieve", "update", "partial_update"]:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]

        elif self.action == "create":
            permission_classes = [IsAuthenticated, ~IsModerator]

        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name="Moderator").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [IsAuthenticated, ~IsModerator]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name="Moderator").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.request.method in ["GET", "PUT", "PATCH"]:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]

        elif self.request.method == "DELETE":
            permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
