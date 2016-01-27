# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Clock
status.register("clock",
    format="%a %-d %b %H:%M:%S",)

# Battery
status.register("battery",
    format="{status} {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS":  "Discharging",
        "CHR":  "Charging",
        "FULL": "Bat full",
    },)

# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="eno1",
    format_up="{v4cidr}",)

# Note: requires both netifaces and basiciw
status.register("network",
    interface="wlp2s0",
    format_up="{essid} {quality:3.0f}%",)

# Shows alsa default sink volume
status.register("alsa",
    format="♪{volume}",)

status.run()
