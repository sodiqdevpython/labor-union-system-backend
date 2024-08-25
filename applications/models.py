from django.db import models
from utils.models import BaseModel
from utils.choices import ApplicationStatus


class Application(BaseModel):
    user = models.ForeignKey("employee.Employe", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    body = models.TextField()
    status = models.CharField(max_length=2, choices=ApplicationStatus.choices, default=ApplicationStatus.send)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"