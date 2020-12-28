#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json

urlCom = "http://api.qqpusher.yanxianjun.com/"
urlPro = 'http://api.qqpusherpro.yanxianjun.com/'


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
        url = urlCom + "send_private_msg"
        data = {
            "token": self.token,
            "user_id": self.id,
            "message": message,
            "auto_escape": self.auto_escape
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_group_msg(self, message):
        """
        发送群消息
        :param message: 消息内容
        :return: 状态码
        """
        url = urlCom + "send_group_msg"
        data = {
            "token": self.token,
            "group_id": self.id,
            "message": message,
            "auto_escape": self.auto_escape
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def set_group_mute_all(self, isMute):
        """
        全部禁言
        :param isMute: True(设置禁言) or False(取消禁言)
        :return: 状态码
        """
        url = urlCom + "set_group_mute_all"
        data = {
            "token": self.token,
            "group_id": self.id,
            "mute": isMute
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def set_group_mute(self, member_id, mute_time):
        """
        禁言单个成员
        :param member_id: 成员QQ号，整形
        :param mute_time: 禁言时间，整形，单位：秒
        :return: 状态码
        """
        url = urlCom + "set_group_mute"
        data = {
            "token": self.token,
            "group_id": self.id,
            "group_member": member_id,
            "mute_time": mute_time
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def set_group_name(self, group_name):
        """
        设置群名
        :param group_name: 群名
        :return: 状态码
        """
        url = urlCom + "set_group_name"
        data = {
            "token": self.token,
            "group_id": self.id,
            "group_name": group_name
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def set_group_memo(self, memo):
        """
        设置群公告
        :param memo: 群公告
        :return: 状态码
        """
        url = urlCom + "set_group_memo"
        data = {
            "token": self.token,
            "group_id": self.id,
            "memo": memo
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res


class qqpusherpro(object):
    def __init__(self, token, bot):
        self.token = token
        self.bot = bot

    def register(self, username, pwd, user_tag):
        url = urlPro + 'reg'
        data = {
            "user_name": username,
            "user_password": pwd,
            "user_tag": user_tag,
            "token": self.token
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def add_qq(self, password):
        url = urlPro + 'add_qq'
        data = {
            "token": self.token,
            "bot": self.bot,
            "password": password,
            "enable": True
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def login(self):
        url = urlPro + 'login'
        data = {
            "token": self.token,
            "bot": self.bot
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def logout(self):
        url = urlPro + 'logout'
        data = {
            "token": self.token,
            "bot": self.bot
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def get_state_info(self):
        url = urlPro + 'get_state_info'
        data = {
            "token": self.token,
            "bot": self.bot
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_friend_msg(self, qq, msg):
        url = urlPro + 'send_friend_msg'
        data = {
            "token": self.token,
            "bot": self.bot,
            "qq": qq,
            "msg": msg
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_friend_json(self, qq, json):
        url = urlPro + 'send_friend_json'
        data = {
            "token": self.token,
            "bot": self.bot,
            "qq": qq,
            "json": json
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_friend_xml(self, qq, xml):
        url = urlPro + 'send_friend_xml'
        data = {
            "token": self.token,
            "bot": self.bot,
            "qq": qq,
            "xml": xml
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_group_msg(self, group, msg):
        url = urlPro + 'send_group_msg'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "msg": msg
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_group_json(self, group, json):
        url = urlPro + 'send_friend_json'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "json": json
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def send_group_xml(self, group, xml):
        url = urlPro + 'send_friend_xml'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "xml": xml
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def add_friend(self, qq, msg):
        url = urlPro + 'add_friend'
        data = {
            "token": self.token,
            "bot": self.bot,
            "qq": qq,
            "msg": msg
        }
        res = requests.post(url=url, data=json.dumps(data))
        return data

    def delete_friend(self, qq):
        url = urlPro + 'delete_friend'
        data = {
            "token": self.token,
            "bot": self.bot,
            "qq": qq
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def handle_friend_event(self, qq, method, msg):
        url = urlPro + 'handle_friend_event'
        data = {
            "token": self.token,
            "bot": self.bot,
            "qq": qq,
            "method": method,
            "msg": msg
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def join_group(self, group, msg):
        url = urlPro + 'join_group'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "msg": msg
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def quit_group(self, group):
        url = urlPro + 'quit_group'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def all_ban(self, group, enable):
        url = urlPro + 'all_ban'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "enable": enable
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def ban(self, group, qq, block):
        url = urlPro + 'ban'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "qq": qq,
            "block": block
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def kick_group_member(self, group, qq):
        url = urlPro + 'kick_group_member'
        data = {
            "token": self.token,
            "bot": self.bot,
            "group": group,
            "qq": qq,
            "block": True
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res

    def add_event(self, bot_event_host, bot_event_url):
        url = urlPro + 'add_event'
        data = {
            "token": self.token,
            "bot": self.bot,
            "bot_event_host": bot_event_host,
            "bot_event_url": bot_event_url
        }
        res = requests.post(url=url, data=json.dumps(data))
        return res
