import qqpusher
import os
import time

Token = os.environ["TOKEN"]
Group_Id = os.environ["GROUP_ID"]
Private_Id = os.environ["PRIVATE_ID"]

if __name__ == '__main__':
    qqpush1 = qqpusher.qqpusher(token=Token, id=Private_Id, auto_escape=False)
    qqpush1.send_private_msg("测试私聊消息")
    time.sleep(10)
    qqpush2 = qqpusher.qqpusher(token=Token, id=Group_Id, auto_escape=False)
    qqpush2.send_group_msg("测试群组消息")
    time.sleep(10)
    qqpush2.set_group_mute_all(True)
    time.sleep(10)
    qqpush2.set_group_mute(Private_Id, 60)
    time.sleep(10)
    qqpush2.set_group_name("测试群名")
    time.sleep(10)
    qqpush2.set_group_memo("测试群公告")
