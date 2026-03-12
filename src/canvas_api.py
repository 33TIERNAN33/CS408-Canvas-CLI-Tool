from datetime import datetime, timedelta, timezone
import requests
from .config import CANVAS_API_TOKEN, CANVAS_BASE_URL

HEADERS = {
    "Authorization": f"Bearer {CANVAS_API_TOKEN}"
}


def _get_paginated(url, params=None):
    all_items = []
    next_url = url
    next_params = params

    while next_url:
        response = requests.get(next_url, headers=HEADERS, params=next_params, timeout=15)

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code} - {response.text}")

        data = response.json()

        if isinstance(data, list):
            all_items.extend(data)
        else:
            return data

        next_params = None
        next_url = response.links.get("next", {}).get("url")

    return all_items


def _filter_out_non_courses(courses):
    filtered = []

    for course in courses:
        name = (course.get("name") or "").lower()

        if "student groups" in name:
            continue
        if "undergrad students" in name:
            continue
        if "bronco ready" in name:
            continue

        filtered.append(course)

    return filtered


def get_all_courses():
    url = f"{CANVAS_BASE_URL}/api/v1/courses"
    params = {
        "enrollment_state": "active",
        "per_page": 100
    }

    courses = _get_paginated(url, params=params)
    return _filter_out_non_courses(courses)


def get_current_courses():
    url = f"{CANVAS_BASE_URL}/api/v1/courses"
    params = {
        "enrollment_state": "active",
        "include[]": ["term"],
        "per_page": 100
    }

    courses = _get_paginated(url, params=params)

    now = datetime.now(timezone.utc)
    recent_cutoff = now - timedelta(days=140)

    filtered = []

    for course in _filter_out_non_courses(courses):
        start_dt = None
        end_dt = None

        start_date = course.get("start_at")
        end_date = course.get("end_at")

        if start_date:
            start_dt = datetime.fromisoformat(start_date.replace("Z", "+00:00"))
        if end_date:
            end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))

        term = course.get("term") or {}
        term_start = term.get("start_at")
        term_end = term.get("end_at")

        if start_dt is None and term_start:
            start_dt = datetime.fromisoformat(term_start.replace("Z", "+00:00"))
        if end_dt is None and term_end:
            end_dt = datetime.fromisoformat(term_end.replace("Z", "+00:00"))

        keep = False

        if end_dt and end_dt >= now:
            keep = True
        elif start_dt and start_dt >= recent_cutoff:
            keep = True
        elif start_dt is None and end_dt is None:
            keep = True

        if keep:
            filtered.append(course)

    return filtered


def get_assignments(course_id):
    url = f"{CANVAS_BASE_URL}/api/v1/courses/{course_id}/assignments"
    params = {
        "per_page": 100
    }

    return _get_paginated(url, params=params)