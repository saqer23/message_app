from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .pusher import pusher_client

class MessagesAPIView(APIView):
    def post(self,request):
        pusher_client.trigger('chat', 'message', {
            'username':request.data['username'],
            'message':request.data['message'],
        })
        return Response([])