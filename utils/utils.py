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
get_link_url = 'https://api.ctext.org/getlink?if=zh&urn='


def read_link(url):
    """
    read content link method, api doc in https://ctext.org/plugins/apilist/zh/#readlink
    :param url: url of a text page
    :return: urn of the page, error
    """
    session = requests.Session()
    resp = session.get(read_link_url + url)
    if not resp.ok:
        print('read %s link failed, response error' % (url, ))
        return None, 1
    json_content = json.loads(resp.content)
    if 'urn' not in json_content:
        print('read %s link failed, json is null' % (url, ))
        return None, 1
    return json_content.get('urn'), None


def get_link(urn):
    session = requests.Session()
    resp = session.get(get_link_url + urn)
    if not resp.ok:
        print('get %s link failed, response error' % (urn,))
        return None, 1
    json_content = json.loads(resp.content)
    if 'url' not in json_content:
        print('get %s link failed, json is null' % (urn,))
        return None, 1
    return json_content.get('url'), None


def get_text(urn):
    session = requests.Session()
    resp = session.get(get_link_url + urn)
    if not resp.ok:
        print('get %s text failed, response error' % (urn,))
        return None, 1
    json_content = json.loads(resp.content)
    if 'fulltext' not in json_content:
        print('get %s text failed, json is null' % (urn,))
        return None, 1
    return json_content, None


if __name__ == '__main__':
    result = read_link('https://ctext.org/nan-jing/jing-mai-zhen-hou/zh')
    print(result[0])
    _result = get_link(result[0])
    print(_result)
