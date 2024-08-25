from django.db.models import TextChoices

class GenderChoice(TextChoices):
    Male = "Male", "Male"
    Female = "Female", "Female"

class HandicappedDegreeChoice(TextChoices):
    Second = "Second", "Second"
    Third = "Third", "Third"

class RoleNoteChoice(TextChoices):
    IronNote = "IN", "Temir daftar"
    WomenNote = "WN", "Ayollar va yoshlar daftari"

class ApplicationStatus(TextChoices):
    send = "sd", "Yuborildi"
    read = "rd", "Ko'rildi"
    approved = "ad", "Qabul qilindi"
    rejected = "rj", "Rad etildi"