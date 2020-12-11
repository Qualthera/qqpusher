## QQPUSHER

> 本项目是[QQPusher](http://qqpusher.yanxianjun.com/)的`Python SDK`
> [QQPusher](http://qqpusher.yanxianjun.com/)的使用方法请参考http://qqpusher.yanxianjun.com/

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

- send_private_msg(self, message)
- send_group_msg(self, message)
- set_group_mute_all(self, isMute)
- set_group_mute(self, member_id, mute_time)
- set_group_name(self, group_name)
- set_group_memo(self, memo)

### 鸣谢

[yanxianjun](https://github.com/yanxianjun)开发维护的[QQPusher推送服务](http://qqpusher.yanxianjun.com/)
