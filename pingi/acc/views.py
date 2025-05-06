import random
import logging
import redis
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Cuser
from .serializers import LoginSerializer

logger = logging.getLogger(__name__)

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data['mobile']
            
            user, created = Cuser.objects.get_or_create(mobile=mobile)
            
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            
            redis_key = f"otp:{mobile}"
            redis_client.set(redis_key, otp)
            redis_client.expire(redis_key, settings.OTP_EXPIRY_SECONDS)
            
            logger.info(f"OTP [{mobile}] -> [{otp}]")
            
            
            return Response({
                'message': 'OTP sent successfully',
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
