# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class YangShTPipeline(object):
    #    def process_item(self, item, spider):
    #        return item

    def __init__(self):
        pass

    def filename(self, item):
        '''
        #print 'item is:', item
        self.INDEX += 1
        return os.path.join(self.DIR, item['cate'], str(self.INDEX)+'.yl.txt.utf8')
        '''
        pass

    def process_item(self, item, spider):
    # def process_item(self, item):
        title = item['title']
        url = item['view_url']

        all_info = []
        all_info.append(title)
        all_info.append(''.join(url))
        file_path = os.path.join(os.getcwd(), 'tt.txt')
        '''
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        all_info.append(title)
        all_info.append(url)
        '''
        with open(file_path, 'aw') as f:
            f.write(' '.join(all_info).encode('utf-8'))
            f.write('\n')

        return
