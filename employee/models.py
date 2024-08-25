from django.db import models
from utils.models import BaseModel
from utils.choices import GenderChoice, HandicappedDegreeChoice, RoleNoteChoice
from django.core.validators import MinLengthValidator, FileExtensionValidator
from django.contrib.auth.models import User

class IdCards(BaseModel):
    id_card = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return self.id_card
    
    class Meta:
        verbose_name = "ID raqam"
        verbose_name_plural = "ID kartalar"


class Profession(BaseModel):
    name = models.CharField(max_length=64, unique=True, validators=[MinLengthValidator(4, message="Bu kasb nomiga o'xshamaydi, kasb nomini to'g'ri kiriting")])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kasb"
        verbose_name_plural = "Kasblar"
    
class UnderAgeChildren(BaseModel):
    user = models.ForeignKey("employee.Employe", on_delete=models.CASCADE, related_name='under_age_children')
    name = models.CharField(max_length=16, validators=[MinLengthValidator(4, "Bolangizni ismini to'g'ri kiriting")])
    born_in = models.DateField()
    metrka = models.FileField(upload_to='employe/under-age-children/', validators=[FileExtensionValidator(allowed_extensions=["pdf","docx", "png", "jpg"], message="Faqat pdf, docx, png, jpg fayl yuklashingiz mumkin")])
    
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} | {self.name}'
    
    class Meta:
        verbose_name = "Voyaga yetmagan farzand"
        verbose_name_plural = "Voyaga yetmagan farzandlar"

class Handicapped(BaseModel):
    user = models.ForeignKey("employee.Employe", on_delete=models.CASCADE, related_name='handicapped')
    group = models.CharField(max_length=6, choices=HandicappedDegreeChoice.choices, default=HandicappedDegreeChoice.Second)
    proof = models.FileField(upload_to='employe/handicapped-docs', validators=[FileExtensionValidator(allowed_extensions=["pdf","docx", "png", "jpg"], message="Faqat pdf, docx, png, jpg fayl yuklashingiz mumkin")])

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "Nogironlik haqida hujjat"
        verbose_name_plural = "Nogironlik haqida hujjatlar"
    
class RoleNote(BaseModel):
    user = models.ForeignKey("employee.Employe", on_delete=models.CASCADE, related_name='role_note')
    note_type = models.CharField(max_length=6, choices=RoleNoteChoice.choices)
    proof = models.FileField(upload_to='employe/note-docs', validators=[FileExtensionValidator(allowed_extensions=["pdf","docx", "png", "jpg"], message="Faqat pdf, docx, png, jpg fayl yuklashingiz mumkin")])

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "Daftar"
        verbose_name_plural = "Daftar"

class Employe(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20, validators=[MinLengthValidator(4, message="Ism juda qisqa, haqiqiy ismga o'xshamaydi")])
    last_name = models.CharField(max_length=20, validators=[MinLengthValidator(6, message="Familiya juda qisqa, haqiqiy familiyaga o'xshamayabdi")])
    father_name = models.CharField(max_length=20, validators=[MinLengthValidator(4, message="Otangizni ismi juda qisqa, haqiqiy ismga o'xshamaydi")])
    born_in = models.DateField()
    gender = models.CharField(max_length=6, choices=GenderChoice.choices)
    employed_at = models.DateField(blank=True, null=True)
    tel_number = models.CharField(max_length=9, unique=True) # +998 ni oldindan kiritilgan bo'ladi
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(upload_to='employe/', default='defaults/defaultUser.png' ,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])])
    score = models.PositiveSmallIntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"