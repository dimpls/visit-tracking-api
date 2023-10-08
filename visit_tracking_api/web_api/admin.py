from django.contrib import admin
from .models import Employee, Store, Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee')
    search_fields = ['name']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    actions = None

    list_display = ('date_time', 'store', 'employee_name', 'latitude', 'longitude')
    search_fields = ['store__name', 'store__employee__name']

    def employee_name(self, obj):
        return obj.store.employee.name

    employee_name.short_description = 'Employee Name'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
