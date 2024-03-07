"""
This file is used to configure the edblog app.
"""
from django.apps import AppConfig


class EdblogConfig(AppConfig):
    """
    This class is used to configure the edblog app.

    **Attributes**
    ``default_auto_field``
        The default auto field for the app.
    ``name``
        The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edblog'
