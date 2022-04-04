from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

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
    
   
    name = models.CharField(max_length=200)
    tags = TaggableManager()
    url = models.CharField(max_length=200)
    tut_format = models.CharField(max_length=20, choices=TUT_FORMAT, default=WRITTEN)
    
    tut_updated = models.DateField()
    difficulty = models.CharField(max_length=20, choices=TUT_DIFFICULTY, default=BEGINNER)
    time = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Tutorials'
        
    def __str__(self):
        return self.name
