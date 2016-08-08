# -*- coding: utf-8 -*-
import json
import urllib

import aes


def make_token(uid):
    '''
    生成用户cookie
    '''
    return aes.encrypt(aes.AES_KEY, json.dumps({'id': uid}))


def parse_token(token):
    '''
    解析用户cookie内容
    '''
    return json.loads(aes.decrypt(aes.AES_KEY, urllib.unquote(token)))


if __name__ == '__main__':
    uid = u'13994595'
    user_cookie = urllib.quote(make_token(uid))
    print 'user_cookie: ', user_cookie   # D8voBwwIgHIJuDMaibPXPsfok5TuJPV2QPsPCJ%2Ba/1g%3D

    c = 'WujrlLPHA0xk39fD90eRLclOSjaXzBK%2F%2FhDGektvFbw%3D'
    parse_uid = parse_token(c)
    print 'parse_uid: ', parse_uid

    c = 'D8voBwwIgHIJuDMaibPXPsfok5TuJPV2QPsPCJ%2Ba/1g%3D'
    parse_uid = parse_token(user_cookie)
    print 'parse_uid: ', parse_uid
