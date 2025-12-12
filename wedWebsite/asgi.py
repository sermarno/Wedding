"""
ASGI config for wedWebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

Usually goes untouched
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedWebsite.settings')

application = get_asgi_application()
