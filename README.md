## QQPUSHER

> 本项目是[QQPusher](http://qqpusher.yanxianjun.com/)的`Python SDK`
> [QQPusher](http://qqpusher.yanxianjun.com/)的使用方法请参考http://qqpusher.yanxianjun.com/

### 本项目的使用

`pip install qqpusher`

**Demo**

> 这里的`id`可以是`qq号`也可是`qq群号`

```python
import qqpusher

if __name__ == '__main__':
    qqpush = qqpusher.qqpusher(token="xxxxxxxx", id="xxxxxxxx", auto_escape=False)
    qqpush.set_group_memo("记得每天打卡喔")

```

**函数列表**

- send_private_msg(self, message)
  - send_private_msg("你好呀")
- send_group_msg(self, message)
  - send_group_msg("大家好")
- set_group_mute_all(self, isMute)
  - set_group_mute_all(True)
- set_group_mute(self, member_id, mute_time)
  - set_group_mute(1018921994, 60)
- set_group_name(self, group_name)
  - set_group_name("测试群名")
- set_group_memo(self, memo)
  - set_group_memo("测试群公告")
    
### 鸣谢

[yanxianjun](https://github.com/yanxianjun)开发维护的[QQPusher推送服务](http://qqpusher.yanxianjun.com/)
