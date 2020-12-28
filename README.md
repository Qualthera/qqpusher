## QQPUSHER

> 本项目是[QQPusher](http://qqpusher.yanxianjun.com/)和[QQPusherPro](http://qqpusherpro.yanxianjun.com/)的`Python SDK`
> [QQPusher](http://qqpusher.yanxianjun.com/)的使用方法请参考http://qqpusher.yanxianjun.com/
> [QQPusherPro](http://qqpusherpro.yanxianjun.com/)的使用方法请参考http://qqpusherpro.yanxianjun.com/

### 本项目的使用

`pip install qqpusher`

**Demo**

> 这里的`id`可以是`qq号`也可是`qq群号`

```python
import qqpusher
import time

Token = "xxxxxxxxxxxxxxxx"
Group_Id = "xxxxxxxxxx"
Private_Id = "xxxxxxxxxx"

if __name__ == '__main__':
    qqpush1 = qqpusher.qqpusher(token=Token, id=Private_Id, auto_escape=False)
    print(qqpush1.send_private_msg("测试私聊消息"))
    time.sleep(10)
    qqpush2 = qqpusher.qqpusher(token=Token, id=Group_Id, auto_escape=False)
    print(qqpush2.send_group_msg("测试群组消息"))
    time.sleep(10)
    print(qqpush2.set_group_mute_all(True))
    time.sleep(10)
    print(qqpush2.set_group_mute(Private_Id, 60))
    time.sleep(10)
    print(qqpush2.set_group_name("测试群名"))
    time.sleep(10)
    print(qqpush2.set_group_memo("测试群公告"))

```

**函数列表**

- qqpusher
    - send_private_msg
    - send_group_msg
    - set_group_mute_all
    - set_group_mute
    - set_group_name
    - set_group_memo
- qqpusherpro
    - get_state_info
    - send_friend_msg
    - send_friend_json
    - send_friend_xml
    - send_group_msg
    - send_group_json
    - send_group_xml
    - add_friend
    - delete_friend
    - handle_friend_event
    - join_group
    - quit_group
    - all_ban
    - ban
    - kick_group_member
    - add_event

### 鸣谢

[yanxianjun](https://github.com/yanxianjun)开发维护的[QQPusher推送服务](http://qqpusher.yanxianjun.com/)
