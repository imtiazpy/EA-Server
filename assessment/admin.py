from django.contrib import admin

from .models import (
    Assessment,
    QuestionTopic,
)


admin.site.register(Assessment)
admin.site.register(QuestionTopic)

