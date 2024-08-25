from rest_framework import serializers
from .models import IdCards, Profession, Employe, RoleNote, Handicapped, UnderAgeChildren

class IdCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdCards
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class RoleNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleNote
        fields = '__all__'

class HandicappedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicapped
        fields = '__all__'

class UnderAgeChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderAgeChildren
        fields = '__all__'