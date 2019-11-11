# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: linus
@Email: linshaofeng1992@gmail.com
@file: utils.py
@time: 2019/11/11 15:39
"""
import requests
import json

read_link_url = 'https://api.ctext.org/readlink?if=zh&url='


def read_link(url):
    session = requests.Session()
    resp = session.get(read_link_url + url)
    if not resp.ok:
        print('get %s link failed, response error' % (url, ))
        return None, 1
    json_content = json.loads(resp.content)
    if 'urn' not in json_content:
        print('get %s link failed, json is null')
        return None, 1
    return json_content.get('urn'), None
