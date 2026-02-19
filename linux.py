import subprocess
import re


def get_active_window():
    try:
        root = subprocess.check_output(['xprop', '-root', '_NET_ACTIVE_WINDOW'])
        wid = re.search(b'0x\w+', root).group(0)

        window = subprocess.check_output(['xprop', '-id', wid, 'WM_NAME'])
        name = re.search(b'"(.*?)"', window).group(1).decode()

        return name if name else "Unknown"
    except Exception:
        return "Unknown"
