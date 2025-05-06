from django.contrib import admin
from .models import Cuser, OTPLog

# Register your models here.

admin.site.register(Cuser)
admin.site.register(OTPLog)