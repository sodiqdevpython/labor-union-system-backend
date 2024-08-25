from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import (
    Employe,
    IdCards, 
    RoleNote,
    Profession, 
    Handicapped,
    UnderAgeChildren,
)

from .serializers import (
    IdCardsSerializer,
    EmployeSerializer,
    RoleNoteSerializer,
    ProfessionSerializer,
    HandicappedSerializer,
    UnderAgeChildrenSerializer
)


class IdCardsView(viewsets.ModelViewSet):
    queryset = IdCards.objects.all()
    serializer_class = IdCardsSerializer


class ProfessionView(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class RoleNoteView(viewsets.ModelViewSet):
    queryset = RoleNote.objects.all()
    serializer_class = RoleNoteSerializer


class HandicappedView(viewsets.ModelViewSet):
    queryset = Handicapped.objects.all()
    serializer_class = HandicappedSerializer


class UnderAgeChildrenView(viewsets.ModelViewSet):
    queryset = UnderAgeChildren.objects.all()
    serializer_class = UnderAgeChildrenSerializer


class EmployeView(APIView):

    def get(self, request, id=None):
        many = False
        if id:
            get_data = get_object_or_404(Employe, id=id)
        else:
            many = True
            get_data = Employe.objects.all()
        
        serializered = EmployeSerializer(get_data, many=many)

        return Response(serializered.data)
    
    def post(self, request):
        get_data = request.data
        serializered = EmployeSerializer(data=get_data)
        if serializered.is_valid():
            serializered.save()
            return Response(serializered.data)
        else:
            return Response(serializered.errors)
        
    def patch(self, request, id, partial=True):
        get_data = request.data
        which_user = get_object_or_404(Employe, id=id)
        serializered = EmployeSerializer(data=get_data, instance=which_user, partial=partial)
        if serializered.is_valid():
            serializered.save()
            return Response(serializered.data)
        else:
            return Response(serializered.errors)
    
    def put(self, request, id, partial=False):
        return self.patch(request, id, partial)
    
    def delete(self, request, id_card):
        if request.user.is_superuser:
            get_user = get_object_or_404(IdCards, id_card=id_card)
            get_user.delete()
            return Response({'status': f"{id_card} o'chirildi"})
        else:
            return Response({'xato': "Faqat yuqori darajadagi admin foydalanuvchini o'chira oladi"})


def errorHandle(request):
    return render(request, '404.html')
