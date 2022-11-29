"""
    Admin configurations for models in GOODUCK_BADUCK project.
"""

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Report, Profile


class Custom_Admin_Site(admin.AdminSite):
    pass

site = Custom_Admin_Site(name="custom_admin_site")  # Instantiating a new AdminSite instance with the extra modifications to the base site

site.site_header = "Goo-D-uck Ba-D-uck Administrator View"
site.index_title = "Whole Site Overview"
site.site_title = "Goo-D-uck Ba-D-uck Admin"
site.empty_value_display = "- - - - -"

@admin.register(Profile, site=site)
class Profile_Admin(admin.ModelAdmin):
    pass

@admin.register(Report, site=site)
class Report_Admin(admin.ModelAdmin):
    pass

@admin.register(User, site=site)
class User_Admin(admin.ModelAdmin):
    pass

# @admin.register(Player, site=site)
# class Player_Admin(admin.ModelAdmin):
#     """ Represents custom formatting when displaying Player objects in Django's
#         AdminSite.
#     """
#
#     fields = (
#         "username",
#         "score",
#         "members_amount",
#         "choices_made",
#         "status",
#         "allowed_host"
#     )
#     list_display = (
#         "username",
#         "score",
#         "members_amount",
#         "status",
#         "allowed_host"
#     )
#     list_filter = ("score", "status", "members_amount", "allowed_host")  # Fields to filter Players upon
#     list_editable = ("score", "allowed_host")  # Fields that can be edited directly in the list view
#     search_fields = ("username",)  # Fields that can be used to search the list view of Players
#
#     def has_add_permission(self, request, obj=None):  # Prevent admins from creating new Player instances without an associated client session
#         return False
#
#
# @admin.register(Game, site=site)
# class Game_Admin(admin.ModelAdmin):
#     """ Represents custom formatting when displaying Game objects in Django's
#         AdminSite.
#     """
#
#     list_display = (
#         "display_current_topic",
#         "display_available_topics",
#         "status",
#         "show_choices"
#     )
#     list_display_links = None  # Ensures Game details are only shown in the list view
#     sortable_by = []
#
#     @admin.display(description="Current Topic")
#     def display_current_topic(self, obj: Game):
#         """ Returns formatted current topic (to display on list view of Game).
#         """
#
#         return f"{obj.current_topic}: {obj}"
#
#     @admin.display(description="Available Topics")
#     def display_available_topics(self, obj: Game):
#         """ Returns formatted list of available topics of the Game (to display
#             on list view of Game).
#         """
#         output_string = ""
#
#         for topic in obj.available_topics:
#             output_string += f"• {topic[0]}: {topic[1]}<br/>"
#
#         return mark_safe(output_string)
#
#     def has_add_permission(self, request, obj=None):  # Prevent admins from creating new Game instances
#         return False
#
#     def has_delete_permission(self, request, obj=None):  # Prevent admins from deleting Game instances
#         return False