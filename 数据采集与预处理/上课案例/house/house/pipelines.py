# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MysqlPipeline:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_spider(self, spider):
        # 数据库连接参数
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='20050110',  # 替换为你的密码
            database='house',  # 替换为你的数据库名
            charset='utf8mb4'
        )
        self.cursor = self.connection.cursor()

        # 创建表（如果不存在）
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS house_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            house VARCHAR(255),
            address VARCHAR(255),
            price VARCHAR(100),
            total VARCHAR(100),
            crawl_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

    def process_item(self, item, spider):
        # 插入数据
        sql = '''
        INSERT INTO house_info (house, address, price, total)
        VALUES (%s, %s, %s, %s)
        '''
        self.cursor.execute(sql, (
            item['house'],
            item['address'],
            item['price'],
            item['total']
        ))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
