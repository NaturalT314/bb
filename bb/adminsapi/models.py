from django.db import models

class Frame(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    stock = models.IntegerField(default=0)
    price_usd = models.FloatField(default=0.0)
    price_gbp = models.FloatField(default=0.0)
    price_eur = models.FloatField(default=0.0)
    price_jod = models.FloatField(default=0.0)
    price_jpy = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Frame"
        verbose_name_plural = "Frames"

    def __str__(self):
        return self.name

class Lens(models.Model):
    PRESCRIPTION_CHOICES = [
        ('fashion', 'Fashion'),
        ('single_vision', 'Single Vision'),
        ('varifocal', 'Varifocal'),
    ]

    LENS_TYPE_CHOICES = [
        ('classic', 'Classic'),
        ('blue_light', 'Blue Light'),
        ('transition', 'Transition'),
    ]

    colour = models.CharField(max_length=50)
    description = models.TextField()
    prescription_type = models.CharField(max_length=15, choices=PRESCRIPTION_CHOICES, default='single_vision')
    lens_type = models.CharField(max_length=20, choices=LENS_TYPE_CHOICES, default='classic')
    stock = models.IntegerField(default=0)
    price_usd = models.FloatField(default=0.0)
    price_gbp = models.FloatField(default=0.0)
    price_eur = models.FloatField(default=0.0)
    price_jod = models.FloatField(default=0.0)
    price_jpy = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Lens"
        verbose_name_plural = "Lenses"

    def __str__(self):
        return f"{self.colour} {self.lens_type} Lens"