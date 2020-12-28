from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, MeetingCreationForm
from .models import CustomUser, Meetings, Members

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'orgName', 'orgNameUrl']

class MeetingsAdmin(admin.ModelAdmin):
    pass
class MembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'orgRef', 'meetRef']
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Meetings, MeetingsAdmin)
admin.site.register(Members, MembersAdmin)
