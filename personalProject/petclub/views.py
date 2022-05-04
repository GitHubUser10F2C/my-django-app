from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class PersonAPIView(APIView):
    def get(self, request):
        return Response(data="estoy en el get del Person", status=200)

    def patch(self, request):
        return Response(data="Estoy en el patch del Person", status=200)

    def delete(self, request):
        return Response(data="Estoy en el delete del Person", status=200)
        
    def post(self, request):
        return Response(data="Estoy en el post del Person", status=200)


class PetAPIView(APIView):
    def get(self, request):
        return Response(data="estoy en el get del Pet", status=200)

    def patch(self, request):
        return Response(data="Estoy en el patch del Pet", status=200)

    def delete(self, request):
        return Response(data="Estoy en el delete del Pet", status=200)

    def post(self, request):
        return Response(data="Estoy en el post del Pet", status=200)
