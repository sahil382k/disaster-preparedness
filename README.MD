# Disaster Preparedness and Response Education System

A Django-based system for schools and colleges to manage disaster preparedness education.

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Features

- Dashboard with preparedness overview
- Module management system
- Virtual drill creation and scheduling
- Alert system with emergency contacts
- Gamification with leaderboards and badges
- Student progress tracking