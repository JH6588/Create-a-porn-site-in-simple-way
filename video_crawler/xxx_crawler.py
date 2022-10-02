import requests
import traceback
import lxml.html
import re
import random

from video.models import Video

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/60.0.3112.113 Safari/537.36"
}


class XXXpron():
    domain = "https://www.xvideos.com"

    def get_video_info(self, url):
        res = requests.get(url, headers=headers)
        tree = lxml.html.fromstring(res.text)
        for ele in tree.cssselect("div#content div[id^=video]"):
            item = {}
            try:
                video_url = self.domain + ele.cssselect("p a[title]")[0].get("href")
                print(video_url)
                item['video_url'] = video_url
                item['video_link'] = self.get_video_link(video_url)
                # video_image_text= ele.cssselect("img['data-videoid']")[0].text
                item['video_image'] = ele.cssselect("img[data-videoid]")[0].get("data-src")
                item['video_length'] = ele.cssselect("p.metadata span.duration")[0].text
                item['video_source'] = "xvideos"
                item['video_title'] = ele.cssselect("p a[title]")[0].text

                # 由于网站改版删除了原来的 quality字段 ，所以现在直接将其设为随机
                item['video_quality'] = random.randint(50, 90)
                # item["video_views"] = ele.cssselect("span.bg span.mobile-hide")[0].text.replace("% -","").strip()

                yield item
            except Exception as e:
                print("错误:{}".format(e))
                traceback.print_exc()

    @staticmethod
    def get_video_link(url):

        res = requests.get(url, headers=headers)
        html = res.text

        video_link = re.search("setVideoUrlHigh\('(.*?)'\)", html).group(1)
        return video_link
        # res = requests.get(link)
        # with open("E:/my/video/fun/{}.mp4".format(name), "wb") as f:
        #     f.write(res.content)

    def insert_video(self, search, page):
        goal_url = "https://www.xvideos.com/?k={}&p={}".format(search, page)
        for item in self.get_video_info(goal_url):
            v = Video(video_link=item['video_link'], video_url=item['video_url'], video_image=item['video_image'],
                      video_length=item['video_length'],
                      video_title=item['video_title'], video_keyword=search, video_quality=item['video_quality'],
                      video_source=item['video_source'])
            print(v)
            v.save()


if __name__ == '__main__':
    x = XXXpron()
    print(x.get_video_link("https://www.xvideos.com/video30033955/schoolgirls_sweet_blowjobs"))
