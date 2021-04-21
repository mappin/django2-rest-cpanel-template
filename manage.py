#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 
        #'config.settings.{0}'.format(os.environ.setdefault('DJANGO_ENV', 'test'))  # test
        'config.settings.{0}'.format(os.environ.setdefault('DJANGO_ENV', 'development'))  # development
        #'config.settings.{0}'.format(os.environ.setdefault('DJANGO_ENV', 'development'))  # production
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
