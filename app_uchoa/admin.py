from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Area)
admin.site.register(Cobrador)
admin.site.register(Emprestimo)
admin.site.register(Parcela)
admin.site.register(ValeRua)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)