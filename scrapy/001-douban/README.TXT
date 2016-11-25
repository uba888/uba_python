#v1.0 excutetime:360s

https://movie.douban.com/top250

标题：
title=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]//span[1][@class="title"]/text()').extract()
url:
href=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]/div/a/@href').extract()
简介：
xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]/div[@class="bd"]/p[1]').xpath('string(.)').extract()

评分：
score=xp.xpath('//ol[@class="grid_view"]/li//div[@class="info"]//span[@class="rating_num"]/text()').extract()

后页：
xp.xpath('//span[@class="next"]/a/@href').extract()[0]
https://movie.douban.com/top250 ?start=25&filter=


观看地址：
xp2.xpath('//ul[@class="bs"]/li/a/text()').extract()
xp2.xpath('//ul[@class="bs"]/li/a/@href').extract()

观看价格：
xp2.xpath('//ul[@class="bs"]/li/span/span/text()').extract()
