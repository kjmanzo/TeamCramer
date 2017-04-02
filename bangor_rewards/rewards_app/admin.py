from django.contrib import admin

# Register your models here.

from .models import Charity
from .models import User
from .models import Achievement
from .models import Activity

admin.site.register(Charity)
admin.site.register(User)
admin.site.register(Achievement)
admin.site.register(Activity)
