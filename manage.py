#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    # Run Daphne WebSockets alongside Django's development server
    if "runserver" in sys.argv:
        try:
            print("Starting Daphne WebSocket server on port 8001...")
            subprocess.Popen(["daphne", "-b", "0.0.0.0", "-p", "8001", "config.asgi:application"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print("Daphne not found! Install it via: pip install daphne")

        # Run Next.js frontend (npm run dev)
        frontend_path = os.path.join(os.path.dirname(__file__), "core", "elearning-ui")
        if os.path.exists(frontend_path):
            try:
                print("Starting Next.js frontend (npm run dev)...")
                subprocess.Popen(["npm", "run", "dev"], cwd=frontend_path,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except FileNotFoundError:
                print("npm not found! Ensure Node.js is installed.")

        # Start Celery worker in the background
        try:
            print("Starting Celery worker...")
            subprocess.Popen(["celery", "-A", "config", "worker", "--loglevel=info"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print("Celery not found! Install it via: pip install celery")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()