#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

class qqpusher(object):
    def __init__(self, token, id, auto_escape):
        self.token = token
        self.id = id
        self.auto_escape = auto_escape

    def send_private_msg(self, message):
        url = "http://api.qqpusher.yanxianjun.com/send_private_msg"
        data = {
            "token": self.token,
            "user_id": self.id,
            "message": message,
            "auto_escape": self.auto_escape
        }
        res = requests.post(url=url, data=data)
        print(res.text)

    def send_group_msg(self, message):
        url = "http://api.qqpusher.yanxianjun.com/send_group_msg"
        data = {
            "token": self.token,
            "group_id": self.id,
            "message": message,
            "auto_escape": self.auto_escape
        }
        res = requests.post(url=url, data=data)
        print(res.text)

    def set_group_mute_all(self, isMute):
        url = "http://api.qqpusher.yanxianjun.com/set_group_mute_all"
        data = {
            "token": self.token,
            "group_id": self.id,
            "mute": isMute
        }
        res = requests.post(url=url, data=data)
        print(res.text)

    def set_group_mute(self, member_id, mute_time):
        url = "http://api.qqpusher.yanxianjun.com/set_group_mute"
        data = {
            "token": self.token,
            "group_id": self.id,
            "group_member": member_id,
            "mute_time": mute_time
        }
        res = requests.post(url=url, data=data)
        print(res.text)

    def set_group_name(self, group_name):
        url = "http://api.qqpusher.yanxianjun.com/set_group_name"
        data = {
            "token": self.token,
            "group_id": self.id,
            "group_name": group_name
        }
        res = requests.post(url=url, data=data)
        print(res.text)

    def set_group_memo(self, memo):
        url = "http://api.qqpusher.yanxianjun.com/set_group_memo"
        data = {
            "token": self.token,
            "group_id": self.id,
            "memo": memo
        }
        res = requests.post(url=url, data=data)
        print(res.text)
