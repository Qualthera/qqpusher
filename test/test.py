import qqpusher

if __name__ == '__main__':
    qqpush1 = qqpusher.qqpusher(token="", id="", auto_escape=False)
    qqpush1.send_private_msg("你好呀")
    qqpush2 = qqpusher.qqpusher(token="", id="", auto_escape=False)
    qqpush2.send_group_msg("大家好")
    qqpush2.set_group_mute_all(True)
    qqpush2.set_group_mute(1018921994, 60)
    qqpush2.set_group_name("测试群名")
    qqpush2.set_group_memo("测试群公告")
