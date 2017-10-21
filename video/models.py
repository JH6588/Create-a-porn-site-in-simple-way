from django.db import models
from  datetime import datetime
# Create your models here.




from  django.db import models
from django.utils import timezone
class Video(models.Model):
    video_link = models.CharField(max_length=500 )
    video_image = models.CharField(max_length=1000 )
    video_length = models.CharField(max_length=255 )
    video_title = models.CharField(max_length=500)
    video_update= models.DateTimeField(default=timezone.now )
    video_day = models.DateField(auto_now_add=True)
    video_keyword = models.CharField(max_length=255)
    video_quality = models.IntegerField(default=0)
    video_url = models.CharField(max_length=1000)
    video_source = models.CharField(max_length=255)
    video_recomend = models.IntegerField(default=0)
    def __str__(self):
        return "video name: {}".format(self.video_title)





