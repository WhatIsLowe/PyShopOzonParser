# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class OzonParserPipeline:
    def close_spider(self, spider):
        """
        После завершения работы парсера вычисляет кол-во вхождений каждой из ОС и сохраняет в виде .txt файла
        """
        # Считывает собранные данные о смартфонах
        df = pd.read_csv('raw_smartphone_data.csv')

        os_counts = df['os_version'].value_counts()
        # Сохраняет полученные данные в формате: id (место в топе) версия_ОС - количество_вхождений
        os_counts.to_csv('top_mobile_os.txt', sep=' - ', index=True, header=False)
