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

    profession = ProfessionSerializer()

    class Meta:
        model = Employe
        fields = ('user', 'name', 'last_name', 'father_name', 'born_in', 'gender', 'employed_at', 'tel_number', 'profession', 'profile_image', 'score', 'is_verified', 'is_admin', )

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