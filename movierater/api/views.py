from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from movierater.api.serializers import GroupSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI

@api_view(['POST'])
def question(request):
    question = request.data.get('question')
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}])
        return Response(response.choices[0].message.content)
    except ValueError:
        return Response({'error': 'Provided number value is not valid integer'}, status=400)