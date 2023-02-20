from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateModified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email