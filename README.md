# Attendance Management

A lightweight command-line attendance lookup tool written in Python. It reads records from `attendance.json` and uses only the Python standard library.

## Requirements

- Python 3.9 or later

No packages or API keys are required.

## Usage

Run commands from this directory:

```bash
python main.py check 1 2026-10-10
python main.py percentage 1
```

The first command reports whether the student was present on that date. The second calculates the percentage from the attendance records, so totals stay in sync with the underlying data.

Use `python main.py --help` for command help. Dates must be valid and use `YYYY-MM-DD` format. Unknown students, missing dates, and invalid data produce an error message.

## Data format

Edit `attendance.json` to add students or attendance dates:

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

Use `true` for present and `false` for absent. The percentage is the number of present days divided by the number of recorded days.

## Project files

- `main.py` — command-line interface and attendance calculations
- `attendance.json` — sample attendance data
- `.gitignore` — excludes Python cache and virtual environment files
