# Canvas CLI Tool

## Description

This project is a Python command-line tool that interacts with the Canvas API. It can list all active courses, list current courses, and display assignments for a selected course. The tool uses environment variables to securely store the Canvas API token, handles pagination for multi-page API results, and formats output into readable terminal tables.

## Demo

![Demo](assets/demo.gif)

## Setup Instructions

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage Examples
List all active courses:
Ex: python -m src.main all-courses

List current courses based off of dates:
Ex: python -m src.main current-courses

List assignments for a course based off of course_id from other usages:
EX: python -m src.main assignments --course-id 12345

## API Endpoints Used
GET /api/v1/courses

GET /api/v1/courses/:course_id/assignments

## Reflection
One challenge in this project was filtering Canvas course results so that old or irrelevant courses did not dominate the output. Another important part was handling pagination, since Canvas can return results across multiple pages. I also focused on formatting the output cleanly so that the tool is more usable from the terminal than raw JSON would be.