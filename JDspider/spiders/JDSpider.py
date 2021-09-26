import scrapy
import re
import json
from JDspider.items import JDCommentItem

# 定义一个爬虫类，继承自scrapy框架的Spider类


class JDSpider(scrapy.Spider):
    # 定义爬虫名，保证在项目中是唯一的
    name = "jdsp"
    header = {
        "Accept-Language": "zh-CN",
        "User-Agent": "Mozilla / 5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.108Safari/537.36"
    }

    # 告诉爬虫从哪个链接开始
    # start_urls = ["https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100002004455&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1"]
    # 默认的解析函数

    def start_requests(self):
        # 手动发起一个请求
        url_format = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100002004455&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1"

        # 爬取10页
        for i in range(2):
            url = url_format.format(i)
            # headers自定义请求头
            # callback指定回调函数
            yield scrapy.Request(url=url, headers=self.header, callback=self.parse)

    def parse(self, response):
        print(response.text)
        sourceStr = response.text
        jsonObj = json.loads(
            re.match("(fetchJSON_comment98\()(.*)(\);)", sourceStr).group(2))
        # print(type(jsonObj))
        # print(jsonObj.keys())
        for comment in jsonObj["comments"]:
            jdCommentItem = JDCommentItem()
            jdCommentItem["nickname"] = comment["nickname"]
            jdCommentItem["score"] = comment["score"]
            jdCommentItem["productColor"] = comment["productColor"]
            jdCommentItem["content"] = comment["content"]
            jdCommentItem["referenceName"] = comment["referenceName"]
            jdCommentItem["referenceTime"] = comment["referenceTime"]
            # 将构建好的Item发送至pipeline进行下一步处理
            yield jdCommentItem
