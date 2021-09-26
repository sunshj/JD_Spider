# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JdspiderPipeline:
    def process_item(self, item, spider):
        print("*"*100)
        print(item["nickname"])
        print("*"*100)

        # 对爬取的数据进行下一步处理
        # 存文件、写数据库
        return item
