from rest_framework.views import APIView
from rest_framework.response import response

# Create your views here.

class FirstAPI(APIView):
    
    def get(self,request)
        return ResPonse(data={'detail':'This is get method of first API'})