import re
import traceback
import lxml.html
import requests
import os
import django


os.environ["DJANGO_SETTINGS_MODULE"] = "sesite.settings"
django.setup()

from video.models import Video

# 240*180

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}


class Pronhub:
    domain = "https://www.pornhub.com"

    def get_video_info(self, url):
        res = requests.get(url, headers=headers)
        html = res.text
        tree = lxml.html.fromstring(html)
        item = {}
        for ele in tree.xpath("//li/div[@class ='wrap']"):
            try:
                video_url = self.domain + ele.xpath(".//a[@data-related-url]/@href")[0]
                item['video_url'] = video_url
                item['video_title'] = ele.xpath(".//a[@data-related-url]/@title")[0]
                item['video_image'] = ele.xpath(".//img/@data-mediumthumb")[0]
                item['video_length'] = ele.xpath(".//var[@class='duration']/text()")[0]
                item['video_quality'] = int(ele.xpath(".//div[@class ='value']/text()")[0].replace("%", "").strip())
                item['video_link'] = Pronhub.get_video_link(video_url)
                item['video_source'] = "pronhub"

                yield item
            except Exception as e:
                print(e)
                print(traceback.print_exc())
                pass

    @staticmethod
    def get_video_link(url):
        res = requests.get(url, headers=headers)
        html = res.text

        video = re.search("480\",\"videoUrl\":\"(.*?)\"}", html).group(1)

        video_link = video.replace("\\", "")
        return video_link

    def insert_video(self, search, page):
        goal_url = "https://www.pornhub.com/video/search?search={}&page={}".format(search, page)
        for item in self.get_video_info(goal_url):
            v = Video(video_link=item['video_link'], video_url=item['video_url'], video_image=item['video_image'],
                      video_length=item['video_length'],
                      video_title=item['video_title'], video_keyword=search, video_quality=item['video_quality'],
                      video_source=item['video_source'])
            print(v)
            v.save()
