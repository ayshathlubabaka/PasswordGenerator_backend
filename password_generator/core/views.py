from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PasswordGenerationSerializer
import random
import string


class PasswordGenerationView(APIView):
    def post(self,request):
        
        serializer = PasswordGenerationSerializer(data=request.data)
        if serializer.is_valid():
            strength = serializer.validated_data.get('strength')
            length = serializer.validated_data.get('length')
            password = self.generate_password(strength,length)
            
            return Response({'password':password}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def generate_password(self,strength,length):
        if strength == 'weak':
            return ''.join(random.choices(string.ascii_lowercase, k=length))
        elif strength == 'medium':
            characters = string.ascii_letters + string.digits
            return ''.join(random.choices(characters, k=length))
        elif strength == 'strong':
            characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choices(characters, k=length))
        else:
            return None
