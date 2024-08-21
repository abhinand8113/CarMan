from django.contrib import admin
from.models import *
# Register your models here.
from.models import driver_reg
admin.site.register(driver_reg)

from.models import driver_login
admin.site.register(driver_login)

from.models import user_reg
admin.site.register(user_reg)

from.models import user_login
admin.site.register(user_login)

admin.site.register(one_way)

admin.site.register(round_trip)

admin.site.register(package)

admin.site.register(admin_login)

admin.site.register(drivertableshow)

admin.site.register(customer_message)