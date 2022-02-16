from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    WRITTEN = 'written'
    VIDEO = 'video'
    TUT_FORMAT = (
        (WRITTEN, 'written'),
        (VIDEO, 'video')
    )
    
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    
    TUT_DIFFICULTY = (
        (BEGINNER, 'beginner'),
        (INTERMEDIATE, 'intermediate'),
        (ADVANCED, 'advanced')
        
    )
    
    category = models.ForeignKey(Category, related_name='tutorials', on_delete=models.CASCADE)
    tut_name = models.CharField(max_length=200)
    tut_link = models.CharField(max_length=200)
    tut_format = models.CharField(max_length=20, choices=TUT_FORMAT, default=WRITTEN)
    tut_tag = models.CharField(max_length=200)
    tut_updated = models.DateField()
    tut_difficulty = models.CharField(max_length=20, choices=TUT_DIFFICULTY, default=BEGINNER)
    tut_time = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Tutorials'
        
    def __str__(self):
        return self.tut_name
