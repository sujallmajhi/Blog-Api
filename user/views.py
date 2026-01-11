from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import action
from .serializers import LoginSerializer

@extend_schema(
    request=LoginSerializer,
    responses={204:None},
    methods=["POST"]
)
@action(detail=True,methods=['POST'])
class Login(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"details": "Required fields missing"}, status=400)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "token": token.key,
                    "user": username,
                    "role": "Admin"
                })
            else:
                return Response(
                    {"error": "Access denied. Only administrators can generate tokens."}, 
                    status=status.HTTP_403_FORBIDDEN
                )
        return Response(
            {"error": "Invalid username or password"}, 
            status=status.HTTP_401_UNAUTHORIZED
        )