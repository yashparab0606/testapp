from django.db import models

class Medicine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    manufacturer_name = models.CharField(max_length=255)
    pack_size_label = models.CharField(max_length=255)
    salt_composition = models.TextField()
    medicine_desc = models.TextField()
    substitute0 = models.CharField(max_length=255, blank=True, null=True)
    substitute1 = models.CharField(max_length=255, blank=True, null=True)
    substitute2 = models.CharField(max_length=255, blank=True, null=True)
    substitute3 = models.CharField(max_length=255, blank=True, null=True)
    substitute4 = models.CharField(max_length=255, blank=True, null=True)
    habit_forming = models.CharField(max_length=50)
    therapeutic_class = models.CharField(max_length=255)
    use0 = models.TextField()
    side_effects = models.TextField()
    image_url = models.URLField(max_length=500)
    
    class Meta:
        db_table = 'medicine'  # Make sure the table name matches the one in your database

