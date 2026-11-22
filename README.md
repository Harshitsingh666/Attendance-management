<div align="center">

# Attendance Management

**A lightweight Python CLI for checking student attendance and calculating attendance rates.**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-standard%20library-2F855A)

</div>

---

## Overview

Attendance Management reads student records from `attendance.json` and provides simple command-line lookups. It uses only Python's standard library, so there is no package installation or service configuration.

## Quick start

```bash
git clone https://github.com/Harshitsingh666/Attendance-management.git
cd Attendance-management
python main.py --help
```

Python 3.9 or newer is required.

## Commands

Check whether a student attended on a date:

```bash
python main.py check 1 2026-10-10
```

Calculate a student's attendance percentage from recorded dates:

```bash
python main.py percentage 1
```

Use the student identifier present in `attendance.json`. Dates use `YYYY-MM-DD`. The CLI reports invalid dates, unknown students, and malformed data.

## Data format

Edit `attendance.json` to maintain the records:

```json
{
  "students": [
    {
      "name": "Sam Example",
      "roll_no": "101",
      "attendance": {
        "2026-10-08": true,
        "2026-10-09": false
      }
    }
  ]
}
```

Use `true` for present and `false` for absent. The percentage is present days divided by recorded days.

## Project layout

```text
.
├── main.py          # CLI commands and attendance calculations
├── attendance.json  # Sample student records
└── README.md
```

## License

No license file is currently listed. Add a license before granting reuse permissions.
