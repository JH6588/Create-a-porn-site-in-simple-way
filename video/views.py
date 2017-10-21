from django.shortcuts import render ,HttpResponse
from django.template import RequestContext, loader
from .models import Video
import binascii, os
from django.utils import timezone
from crawler import video_crawlers_item


# Create your views here.
def create_key():
    return binascii.b2a_base64(os.urandom(50)).decode()



def index(request):
    last_video_list = Video.objects.order_by("video_update")[:10]
    print(last_video_list)
    context ={'last_video_list' :last_video_list }
    return render(request, 'index.html', context)



def refresh_video_link(V):
    return  video_crawlers_item[V.video_source].get_video_link(V.video_url)


def play(request ,vid):
    v = Video.objects.filter(id =vid).first()
    v_update = v.video_update

    if (timezone.now() -v_update).total_seconds() >200:
        print("more than 1 hours  refresh the video link")
        v.video_link = refresh_video_link(v)
        v.video_recomend  =0
        v.save()
    context ={"video_link" :v.video_link ,"video_title":v.video_title}
    return render(request, "play.html", context)

    # return HttpResponse(vid)

def show(request,page):
    page =int(page)
    video_list = Video.objects.all()
    page_num = int(len(video_list) /18) +1
    page_show =range(1,6)
    page_show1 = range(1,page_num)
    video_page_list = video_list[18*(page-1)+1 :18*page+1]

    print(page)
    context = {'video_page_list': video_page_list ,"pagenum": page_num  ,"pageshow" :page_show ,"pageshow1":page_show1 ,"cur_page":page}
    return render(request, 'show.html', context)
