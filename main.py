"""Look up student attendance from the local attendance.json file."""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("attendance.json")


def load_students():
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        students = data["students"]
        if not isinstance(students, list):
            raise ValueError("'students' must be a list")
        return students
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as error:
        raise ValueError(f"Could not load {DATA_FILE.name}: {error}") from error


def find_student(students, roll_no):
    return next((student for student in students if str(student.get("roll_no")) == roll_no), None)


def main():
    parser = argparse.ArgumentParser(description="Check student attendance and percentages.")
    commands = parser.add_subparsers(dest="command", required=True)

    check = commands.add_parser("check", help="Check attendance for a student on a date")
    check.add_argument("roll_no", help="Student roll number")
    check.add_argument("date", help="Date in YYYY-MM-DD format")

    percentage = commands.add_parser("percentage", help="Show a student's attendance percentage")
    percentage.add_argument("roll_no", help="Student roll number")

    args = parser.parse_args()

    try:
        students = load_students()
        student = find_student(students, args.roll_no)
        if student is None:
            parser.error(f"student with roll number {args.roll_no!r} was not found")

        attendance = student.get("attendance", {})
        if args.command == "check":
            try:
                requested_date = date.fromisoformat(args.date).isoformat()
            except ValueError:
                parser.error("date must be a valid date in YYYY-MM-DD format")
            if requested_date not in attendance:
                parser.error(f"no attendance record for {requested_date}")
            status = "Present" if attendance[requested_date] else "Absent"
            print(f"{student['name']} ({student['roll_no']}): {status} on {requested_date}")
        else:
            if not attendance:
                parser.error("student has no attendance records")
            present = sum(value is True for value in attendance.values())
            total = len(attendance)
            print(f"{student['name']} ({student['roll_no']}): {present}/{total} days ({present / total * 100:.2f}%)")
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
