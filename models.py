from django.db import models

class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Alert(models.Model):
    message = models.TextField()
    target_audience = models.CharField(max_length=100)
    geo_fence = models.CharField(max_length=200, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message[:50] + "..."