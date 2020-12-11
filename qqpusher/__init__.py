#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

class qqpusher(object):
    def __init__(self, token, id, auto_escape):
        """
        :param token: QQPusher的Token
        :param id: QQ号或者QQ群号
        :param auto_escape: 消息内容是否作为纯文本发送
        """
        self.token = token
        self.id = id
        self.auto_escape = auto_escape

    def send_private_msg(self, message):
        """
        发送私聊消息
        :param message: 消息内容
        :return: 状态码
        """
        url = "http://api.qqpusher.yanxianjun.com/send_private_msg"
        data = {
            "token": self.token,
            "user_id": self.id,
            "message": message,
            "auto_escape": self.auto_escape
        }
        res = requests.post(url=url, data=data)
        return res

    def send_group_msg(self, message):
        """
        发送群消息
        :param message: 消息内容
        :return: 状态码
        """
        url = "http://api.qqpusher.yanxianjun.com/send_group_msg"
        data = {
            "token": self.token,
            "group_id": self.id,
            "message": message,
            "auto_escape": self.auto_escape
        }
        res = requests.post(url=url, data=data)
        return res

    def set_group_mute_all(self, isMute):
        """
        全部禁言
        :param isMute: True(设置禁言) or False(取消禁言)
        :return: 状态码
        """
        url = "http://api.qqpusher.yanxianjun.com/set_group_mute_all"
        data = {
            "token": self.token,
            "group_id": self.id,
            "mute": isMute
        }
        res = requests.post(url=url, data=data)
        return res

    def set_group_mute(self, member_id, mute_time):
        """
        禁言单个成员
        :param member_id: 成员QQ号，整形
        :param mute_time: 禁言时间，整形，单位：秒
        :return: 状态码
        """
        url = "http://api.qqpusher.yanxianjun.com/set_group_mute"
        data = {
            "token": self.token,
            "group_id": self.id,
            "group_member": member_id,
            "mute_time": mute_time
        }
        res = requests.post(url=url, data=data)
        return res

    def set_group_name(self, group_name):
        """
        设置群名
        :param group_name: 群名
        :return: 状态码
        """
        url = "http://api.qqpusher.yanxianjun.com/set_group_name"
        data = {
            "token": self.token,
            "group_id": self.id,
            "group_name": group_name
        }
        res = requests.post(url=url, data=data)
        return res

    def set_group_memo(self, memo):
        """
        设置群公告
        :param memo: 群公告
        :return: 状态码
        """
        url = "http://api.qqpusher.yanxianjun.com/set_group_memo"
        data = {
            "token": self.token,
            "group_id": self.id,
            "memo": memo
        }
        res = requests.post(url=url, data=data)
        return
