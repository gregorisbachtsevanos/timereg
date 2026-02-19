import time
import datetime
import sys
from activity import DBManager

IDLE_LIMIT = 60  # seconds


# ---------------- IDLE DETECTION ----------------
def get_idle_time():
    if sys.platform.startswith("linux"):
        try:
            import subprocess
            out = subprocess.check_output(["xprintidle"])
            return int(out) / 1000
        except Exception:
            return 0

    elif sys.platform.startswith("win"):
        try:
            import ctypes

            class LASTINPUTINFO(ctypes.Structure):
                _fields_ = [("cbSize", ctypes.c_uint),
                            ("dwTime", ctypes.c_uint)]

            lii = LASTINPUTINFO()
            lii.cbSize = ctypes.sizeof(lii)
            ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
            millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
            return millis / 1000.0
        except Exception:
            return 0

    return 0


# ---------------- WINDOW DETECTION ----------------
def get_active_window():
    if sys.platform.startswith("linux"):
        from linux import get_active_window
        return get_active_window()

    elif sys.platform.startswith("win"):
        import win32gui
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

    elif sys.platform.startswith("darwin"):
        from AppKit import NSWorkspace
        return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

    return "Unknown"


# ---------------- MAIN LOOP ----------------
def run():
    db = DBManager()

    current_activity = get_active_window()
    start_time = datetime.datetime.now()

    print("AutoTimer started...")
    print("Current:", current_activity)

    while True:
        time.sleep(1)

        idle_seconds = get_idle_time()

        if idle_seconds > IDLE_LIMIT:
            new_activity = "Idle"
        else:
            new_activity = get_active_window()

        if new_activity != current_activity:
            end_time = datetime.datetime.now()

            db.add_time_entry(current_activity, start_time, end_time)

            print("Switch:", current_activity, "→", new_activity)

            current_activity = new_activity
            start_time = datetime.datetime.now()


if __name__ == "__main__":
    run()
