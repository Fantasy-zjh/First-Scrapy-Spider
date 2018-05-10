import scrapy
from MySpider.items import MyspiderItem

class TextSpider(scrapy.Spider):
    name = "textspider"
    start_urls=[
        'http://www.dili360.com/cng/tag/index.htm',
    ]
    def parse(self, response):
        content=response.xpath('//div[@class="detail"]/a/@href').extract()
        tips=response.xpath('//div[@class="detail"]/p[1]/text()').extract()
        imgs=response.xpath('//ul[@class="article-list"]/li/div[@class="img"]/img/@src').extract()
        for i,tip,img in zip(content,tips,imgs):
            url="http://www.dili360.com"+i
            yield scrapy.Request(url,callback=lambda arg1=response,arg2=tip,arg3=img:self.parseArticle(arg1,arg2,arg3))
        index=response.xpath('//div[@class="pagination"]/ul/li/text()').extract_first()
        if(index!='6'):
            next_url="http://www.dili360.com"+response.xpath('//div[@class="pagination"]/ul/a/@href').extract()[-1]
            yield scrapy.Request(next_url,callback=self.parse)
    def parseArticle(self,response,p,image):
        item=MyspiderItem()
        item['article_title']=response.xpath('//div[@class="common-article-page"]/article/h1/text()').extract_first()
        item['article_subtitle']=response.xpath('//div[@class="common-article-page"]/article/h1/span/text()').extract_first()
        item['article_bodyhtml']=response.xpath('//div[@class="common-article-page"]/article/section').extract_first()
        item['article_author']=response.xpath('//div[@class="common-article-page"]/article//a[@class="link blue"]/text()').extract_first()
        item['article_date']=response.xpath('//div[@class="common-article-page"]/article/p[1]/a[1]/text()').extract_first()
        item['article_theme']=p
        item['article_img']=image
        imgs=response.xpath('//div[@class="common-article-page"]/article/section/div[@class="imgbox"]/div[@class="img"]/img/@src').extract()
        str=''
        for img in imgs:
            str=str+img+'$'
        item['article_imgs']=str[0:-1]
        all_text = response.xpath('//div[@class="common-article-page"]/article/section//p/text()').extract()
        str2=''
        for text in all_text:
            str2=str2+text+'$'
        item['article_text']=str2[0:-1]
        yield item