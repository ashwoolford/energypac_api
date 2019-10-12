from django.db import models

class Opportunity(models.Model):
    opportunity_name = models.CharField(max_length=100, blank=False)
    opportunity_type = models.CharField(max_length=100)
    lead_source = models.CharField(max_length=100)
    amount = models.CharField(max_length=100, blank=False)
    close_date = models.CharField(max_length=20, blank=False)
    opportunity_status = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
