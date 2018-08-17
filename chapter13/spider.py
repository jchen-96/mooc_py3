import re
from urllib import request


class Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattent = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_arr = re.findall(Spider.root_pattern, htmls, re.S)
        print(str(root_arr.__len__())+'\n********************')
        anchols = []
        for video_info in root_arr:
            name = re.findall(Spider.name_pattent, video_info, re.S)
            number = re.findall(Spider.number_pattern, video_info, re.S)
            anchols.append({'name': name, 'number': number})
        return anchols

    def __redefine(self, anchols):
        l = lambda x: {'name': x['name'][0].strip(), 'number': x['number'][0]}
        anchols = map(l, anchols)
        return anchols

    def __sort_seed(self, ahchol):
        r = re.findall('\d*', ahchol['number'])
        number = float(r[0])
        if '万' in ahchol['number']:
            number *= 10000
        return number

    def __sort(self, anchols):
        anchols = sorted(anchols, key=self.__sort_seed, reverse=True)
        return anchols

    def __show(self, anchols):
        for rank in range(0,len(anchols)):
            print(
                ' rank:  '+str(rank+1)+
                '    '+anchols[rank]['name']+
                '    '+anchols[rank]['number']+'人'
            ) 

    def go(self):
        html = self.__fetch()
        anchols = self.__analysis(html)
        anchols = self.__redefine(anchols)
        anchols = self.__sort(anchols)
        self.__show(anchols)


spider = Spider()
spider.go()
