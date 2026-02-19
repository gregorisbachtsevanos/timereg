# AutoTimer — Automatic Desktop Activity Tracker

AutoTimer is a lightweight cross-platform desktop activity tracker that automatically records how much time you spend on applications and websites by monitoring the active window on your system.

The app runs in the background, detects window changes, and stores activity durations in a JSON file for later analysis.

---

## Features

* Automatic active window tracking
* Website detection when using Google Chrome
* Cross-platform support (Windows, macOS, Linux)
* Persistent activity storage using JSON
* Object-oriented data model
* Continuous background monitoring
* Per-activity time breakdown (days, hours, minutes, seconds)

---

## Project Structure

```
project/
│
├── autotimer.py        # Main tracking loop
├── activity.py         # Data models & JSON serialization
├── linux.py            # Linux window detection support
├── activities.json     # Generated activity data
└── README.md
```

---

## ⚙️ How It Works

1. The app continuously checks the active window every second.
2. When a window change is detected:

   * The previous activity is closed
   * A time entry is created
   * The entry is added to the corresponding activity
3. Activities are stored in `activities.json`.

If Google Chrome is active, the app extracts the domain from the current tab and tracks time per website.

---

## Data Model

### ActivityList

* Stores all activities
* Handles JSON loading and saving

### Activity

* Represents a tracked app or website
* Contains multiple time entries

### TimeEntry

* Start time
* End time
* Computed duration breakdown

---

## Installation

### 1. Clone repository

```
git clone <repo-url>
cd <repo-folder>
```

### 2. Install dependencies

```
pip install python-dateutil
```

### 3. Platform-specific requirements

#### Windows

```
pip install pywin32 uiautomation
```

#### macOS

Requires:

* PyObjC
* AppleScript permissions

#### Linux

Requires:

```
xprop
```

Install via:

```
sudo apt install x11-utils
```

---

## Usage

Run:

```
python autotimer.py
```

Stop with:

```
CTRL + C
```

Activity data will be saved automatically.

---

## Example JSON Output

```json
{
  "activities": [
    {
      "name": "YouTube",
      "time_entries": [
        {
          "start_time": "2026-02-19 10:00:00",
          "end_time": "2026-02-19 10:30:00",
          "days": 0,
          "hours": 0,
          "minutes": 30,
          "seconds": 0
        }
      ]
    }
  ]
}
```

---

## Known Limitations

* No idle detection
* No GUI dashboard
* Chrome-only browser tracking
* Linux support depends on X11
* Background service mode not implemented
* Limited error handling

---

## Future Improvements

* Idle time detection
* GUI dashboard with charts
* Multi-browser support
* Productivity scoring
* Background service/daemon mode
* Weekly & monthly reports
* Database storage instead of JSON
* Export to CSV / Excel
* Notifications & reminders

---

## Contributing

Pull requests and feature suggestions are welcome.

---

## License

MIT License
