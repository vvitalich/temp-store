from django.contrib import admin

from .models import Car, Enterprise, EnterpriseMembership, UserProfile, PhoneNumber


# @admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_first_name', 'get_last_name', 'image', 'passenger']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'
    # list_filter = ['role']

    # def get_roles(self, obj):
    #     return ", ".join([role.role for role in obj.role.all()])

    # def delete_model(self, request, obj):
    #     obj.user.delete()  # Удаление пользователя вместе с профилем
    #     super().delete_model(request, obj)


class CarAdmin(admin.ModelAdmin):
    list_display = ('number_car', 'model_car', 'enterprise', 'passengers_capacity', 'cargo_capacity', 'has_pets_allowed')


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'user', 'enterprise', 'messenger')


class EnterpriseMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'enterprise', 'position')


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(EnterpriseMembership, EnterpriseMembershipAdmin)

