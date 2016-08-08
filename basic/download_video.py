# -*- coding: utf-8 -*-
import logging
import requests
import traceback
import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import json
logger = logging.getLogger(__name__)
vinfo = 'http://vv.video.qq.com/getinfo?vids=%s&otype=json'
vkey = 'http://vv.video.qq.com/getkey?format=%s&filename=%s&otype=json&vid=%s&vt=%s'

furl = '%s%s?sdtfrom=v3010&type=mp4&vkey=%s&platform=2&fmt=auto&sp=0&br=%s'



class GetVideo:
    def __init__(self,url):
        self.url= url

    def get_video_url(self):
        raise NotImplementedError

    def _request(self,url):
        return requests.get(url).text


class QQVideo(GetVideo):

    def _get_vid(self):
        vid=None
        try:
            vid = urlparse.parse_qs(urlparse.urlparse(self.url).query)['vid'][0]

        except:
            pass
        return vid

    def get_video_url(self):
        vid=self._get_vid()
        return processurl(self.url,vid)


def extract_param(url, vid):
    text = urllib2.urlopen(url).read()
    p = re.compile('\{.*\}')
    d = p.search(text).group(0)

    data = json.loads(d)
    fn = data['vl']['vi'][0]['fn']
    keyid = data['vl']['vi'][0]['cl']['ci'][0]['keyid'].split('.')[-1]
    fname = fn.replace('2.mp4', keyid) + '1.mp4'

    fmts = [i['id'] for i in data['fl']['fi'] if i['name'] in ('hd', 'sd', 'mp4')]#[0]
    fmt = [i for i in fmts if len(str(i)) > 1][0]
    url = data['vl']['vi'][0]['ul']['ui'][0]['url']

    vt = data['vl']['vi'][0]['ul']['ui'][0]['vt']
    br = data['vl']['vi'][0]['br']

    return (fmt, fname, vid, vt), (url, br, fname)


def getfkey(url):
    text = urllib2.urlopen(url).read()
    p = re.compile('\{.*\}')
    d = json.loads(p.search(text).group(0))

    return d['key']


def processurl(url, vid):
    """
    http://v.qq.com/cover/x/xieircansk35gpt.html?vid=j0139bs5eup
    """
    #if 'vid=' not in url:
    #    vid = url.split('/')[-1].split('.')[0]
    #else:
    #    vid = url.split('vid=')[-1]
    #    if '&' in vid:
    #        vid = vid.split('&')[0]
    try:
        infourl = vinfo % vid

        v, x = extract_param(infourl, vid)

        u = vkey % v

        gkey = getfkey(u)

        prefix = x[0]
        br = x[1]
        fn = x[-1]

        param = (prefix, fn, gkey, br)

        return furl % param
    except:
        url = 'http://vv.video.qq.com/geturl?otype=json&platform=1&ran=0.9652906153351068&vid='+vid
        data = urllib2.urlopen(url).read()
        return json.loads(data[data.find('QZOutputJson=')+13:-1])['vd']['vi'][0]['url']

def video_parse(url):
    netloc = urlparse.urlparse(url).netloc
    v=None
    if netloc=='www.miaopai.com':
        # v = MiaopaiVideo(url)
        pass
    elif netloc=='m.miaopai.com':
        # v = MiaopaiVideo(url)
        pass
    elif netloc=='m.v.qq.com' or netloc=='v.qq.com':
        v = QQVideo(url)
    elif netloc == 'v.youku.com':
        # v = YoukuVideo(url)
        pass
    elif 'gifshow.com' in netloc or 'kuaishou.com' in netloc:
        # v = GifshowVideo(url)
        pass
    return v



def get_video_type(url):
    if url.find('miaopai') != -1:
        return 'miaopai'
    elif url.find('mp.weixin') != -1:
        return 'weixin'
    elif url.find('qq.com') != -1:
        return 'qq'
    elif 'v.youku.com' in url:
        return 'youku'
    elif 'gifshow.com' in url or 'kuaishou.com' in url:
        return 'gifshow'
    else:
        return 'unknown'


def geturls_by_frame(url):
    buffer = requests.get(url)
    if buffer.status_code != requests.codes.ok:
        logger.info('process_url request url error  %s' % buffer.status_code)
        return {}
    body = buffer.text
    soup = BeautifulSoup(body)
    match2 = re.findall('<iframe class="video_iframe" .* (data-)?src="(\S*)" .*></iframe>', body)
    match1 = re.findall('(http(s)?://v.qq.com/iframe/\S*)\"', body)
    if match1:
        try:
            parser_url = video_parse(match1[0][0])
            video_url = parser_url.get_video_url()
            video_type = get_video_type(match1[0][0])
            return {'video': video_url, 'title': soup.title.string, 'video_type': video_type}
        except:
            logger.info('process_url error match1 %s' % url)
            return {}
    elif match2:
        try:
            parser_url = video_parse(match2[0][1])
            video_url = parser_url.get_video_url()
            video_type = get_video_type(match1[0][0])
            return {'video': video_url, 'title': soup.title.string, 'video_type': video_type}
        except:
            logger.info('process_url error match2 %s' % url)
            return {}
    else:
        if not soup.find(id='js_content'):
            logger.info('process_url error longtxt can not process %s' % url)
            return {}
        return {'longtxt': body, 'title': soup.title.string}


def download_video(ori_uri, dest_path_file):
    try:
        print '====download_video===='
        headers = {'user-agent': 'mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 MicroMessenger/5.0'}
        r = requests.get(ori_uri, timeout=1800, headers=headers)
        with open(dest_path_file, "wb") as code:
            code.write(r.content)
    except Exception, e:
        logger.info('process_url download video failed %s(%s)', ori_uri, e)
        print traceback.print_exc()
        return ''



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    url = 'http://mp.weixin.qq.com/s?__biz=MjM1ODIzNTU2MQ==&mid=411582263&idx=3&sn=1b0506956ce854254ae17017c9827102&scene=2&srcid=0401ykjTfNlfTH787chp4ly3&from=timeline&isappinstalled=0#wechat_redirect'
    # url = 'http://mp.weixin.qq.com/s?__biz=MzIzOTA3NTA5Mg==&mid=403778897&idx=1&sn=2b2b607bcb23646507e1d6097daf77e6&scene=0#wechat_redirect'
    result = video_parse(url)

    if not result:
        # 从iframe中提取
        result = geturls_by_frame(url)

    video_url = result['video']
    video_type = get_video_type(url)
    print video_url
    # print video_type

    # download_video(video_url, "/home/andy/test.mp4")