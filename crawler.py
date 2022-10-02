from video_crawler.hub_crawler import Pronhub
from video_crawler.xxx_crawler import XXXpron
from video.models import Video
import time
import random
from datetime import date

T = 3600
video_crawlers_item = {'pronhub': Pronhub, "xvideos": XXXpron}
key_words_1 = ["chinese couples", "chinese", "taiwan", "korea", "china", "chinese girl", "asia", "asia girl"]
key_words_2 = ["3p", "blow job", "sm", "fuck", "girl", "beautiful", "women", "party"]


def wash_video(days=1):
    for v in Video.objects.all():
        _days = (date.today() - v.video_day).days
        if _days > days:
            v.delete()
        elif _days == days:
            v.video_recomend = 1  # 不推荐


def sleep_activate_orm(t):  # t 为小时数
    for i in range(t):
        time.sleep(T)
        print(Video.objects.all().count())


if __name__ == '__main__':

    xxx = XXXpron()
    hub = Pronhub()
    T = 60

    while True:
        m = 0
        for i, j in zip(key_words_1, key_words_2):
            v_size = len(Video.objects.all())
            print("现存视频量：{}".format(v_size))
            k = random.randint(1, 20)
            hub.insert_video(i, k)
            hub.insert_video(j, k)
            print("暂停 {}".format(T))
            time.sleep(T)
            xxx.insert_video(i, k)
            xxx.insert_video(j, k)
            #     for obj in Video.objects.order_by("video_update")[:v_size/]:
            #         obj.delete()
            print("暂停 {}".format(T))
            sleep_activate_orm(11)  # 需
            m += 1
            if m == 2:
                wash_video(days=1)
                m = 0
