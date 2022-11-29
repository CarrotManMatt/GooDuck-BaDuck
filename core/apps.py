"""
    App configurations in core.
"""

from django.contrib.admin.apps import AdminConfig


class Custom_Admin_Config(AdminConfig):
    """ Represents configurations of custom implementation of Django's
        AdminSite
    """

    default_site = "app.admin.Custom_Admin_Site"