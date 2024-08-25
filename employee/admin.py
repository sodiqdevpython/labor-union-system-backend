from django.contrib import admin
from .models import Profession, UnderAgeChildren, Handicapped, RoleNote, Employe, IdCards

@admin.register(IdCards)
class IdCardsAdmin(admin.ModelAdmin):
    list_display = ('id_card', )
    search_fields = ('id_card', )

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(UnderAgeChildren)
class UnderAgeChildrenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'born_in', 'is_approved')
    search_fields = ('name', 'user__name')
    list_filter = ('is_approved', 'born_in')
    date_hierarchy = 'born_in'
    ordering = ('-born_in',)
    autocomplete_fields = ['user']

@admin.register(Handicapped)
class HandicappedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'is_approved')
    search_fields = ('user__name', 'group')
    list_filter = ('group', 'is_approved')
    ordering = ('group',)
    autocomplete_fields = ['user']

@admin.register(RoleNote)
class RoleNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'note_type', 'is_approved')
    search_fields = ('user__name', 'note_type')
    list_filter = ('note_type', 'is_approved')
    ordering = ('note_type',)
    autocomplete_fields = ['user']

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'father_name', 'born_in', 'gender', 'profession', 'is_verified', 'is_admin', 'created', 'updated')
    search_fields = ('name', 'last_name', 'tel_number', 'profession__name')
    list_filter = ('gender', 'is_verified', 'is_admin', 'profession', 'born_in')
    date_hierarchy = 'born_in'
    ordering = ('last_name', 'name')
    autocomplete_fields = ['profession']
    list_per_page = 20