from django.contrib import admin
from .models import UserEmail as UserEmailModel
from .models import UserMessage as UserMessageModel
# from .models import User as UserModel
# Register your models here.

# admin.site.register(UserModel   )
admin.site.register(UserEmailModel)
admin.site.register(UserMessageModel)
