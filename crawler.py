from video_crawler.hub_crawler import Pronhub
from video_crawler.xxx_crawler import XXXpron
from video.models import Video
import time
import random
from datetime import date
video_crawlers_item ={'pronhub' :Pronhub ,"xvideos":XXXpron}
key_words_1 = ["chinese", "taiwan", "korea", "china", "chinese girl" ,"asia" ,"asia girl" ]
key_words_2 = ["3p", "blow job", "sm" ,"fuck" ,"girl" ]

if __name__ == '__main__':

    xxx =XXXpron()
    hub = Pronhub()
    T =3600



    while True:

        for i ,j in zip(key_words_1 ,key_words_2):
            for v in Video.objects.all():
                _days = (date.today() - v.video_day).days
                if _days > 1:
                    v.delete()
                elif _days == 1:
                    v.video_recomend = 1
            v_size = len(Video.objects.all())
            print("now the pron video numbers：{}".format(v_size))
            k = random.randint(1,15)
            xxx.insert_video(i,k)
            xxx.insert_video(j,k)
            print("sleep {}".format(T))
            time.sleep(T)
            hub.insert_video(i,k)
            hub.insert_video(j,k)
            # for obj in Video.objects.order_by("video_update")[:v_size]:
            #     obj.delete()
            print("sleep {}".format(T))
            for i in range(3):
                time.sleep(T * 4)
                print(Video.objects.all().count())