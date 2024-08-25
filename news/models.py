from django.db import models
from utils.models import BaseModel
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class News(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='news/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'webp'], message="faqat rasm (png, jpg, webp) fayl yuklashingiz mumkin !")])
    text = models.TextField()
    author = models.ForeignKey("employee.Employe", on_delete=models.CASCADE)
    views = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

class Comment(BaseModel):
    text = models.CharField(max_length=1024)
    news_comment = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[0:10]} ...'
    
    class Meta:
        verbose_name = "Komentariya"
        verbose_name_plural = "Komentariyalar"