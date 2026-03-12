from datetime import datetime
from tabulate import tabulate


def _format_canvas_date(date_string):
    if not date_string:
        return "No due date"

    try:
        dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return date_string


def print_courses(courses):
    courses = sorted(courses, key=lambda c: (c.get("name") or "").lower())
    table = []

    for course in courses:
        table.append([
            course.get("id", "N/A"),
            course.get("name") or "Unnamed Course",
            course.get("course_code", "N/A"),
            course.get("start_at", "N/A"),
            course.get("end_at", "N/A")
        ])

    print(tabulate(
        table,
        headers=["Course ID", "Course Name", "Course Code", "Start", "End"]
    ))


def print_assignments(assignments):
    assignments = sorted(assignments, key=lambda a: a.get("due_at") or "")

    table = []
    for assignment in assignments:
        table.append([
            assignment.get("id", "N/A"),
            assignment.get("name", "Unnamed Assignment"),
            _format_canvas_date(assignment.get("due_at"))
        ])

    print(tabulate(table, headers=["ID", "Assignment", "Due Date"]))