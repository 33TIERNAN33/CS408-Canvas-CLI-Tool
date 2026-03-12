import argparse
from .canvas_api import get_all_courses, get_current_courses, get_assignments
from .formatter import print_courses, print_assignments


def run_cli():
    try:
        parser = argparse.ArgumentParser(description="Canvas CLI Tool")

        parser.add_argument(
            "command",
            choices=["all-courses", "current-courses", "assignments"],
            help="Command to run"
        )

        parser.add_argument(
            "--course-id",
            type=int,
            help="Course ID for assignments command"
        )

        args = parser.parse_args()

        if args.command == "current-courses":
            courses = get_current_courses()
            print_courses(courses)

        elif args.command == "all-courses":
            courses = get_all_courses()
            print_courses(courses)

        elif args.command == "assignments":
            if not args.course_id:
                print("Please provide --course-id")
                return

            assignments = get_assignments(args.course_id)
            print_assignments(assignments)

    except Exception as e:
        print(f"Error: {e}")