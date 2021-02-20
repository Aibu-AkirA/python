import scrapy

class exam8Spider(scrapy.Spider):
    name = 'exam8'
    start_urls = [
      'file://c/temp/kujira.html'
    ]

    def parse(self, response):
        # URLリンク情報を抽出
        li_list =
        for a in li_list:
            # href属性とテキストを取り出す
            href =
            text =
            # 結果を戻す