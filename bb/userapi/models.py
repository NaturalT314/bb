from django.db import models
from adminsapi.models import Frame, Lens

class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Glasses(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
    frame_price_usd = models.FloatField()
    lens_price_usd = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Glasses"
        verbose_name_plural = "Glasses"

    def __str__(self):
        return f"{self.frame.name} with {self.lens.colour} Lens"

    def total_price_usd(self):
        return self.frame_price_usd + self.lens_price_usd
    
