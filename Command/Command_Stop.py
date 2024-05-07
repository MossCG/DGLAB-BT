import BasicIO


def cmd_stop():
    BasicIO.output_command("msg", "DGLAB蓝牙核心已关闭！")
    BasicIO.output_command("event", "stop")
    exit(0)
