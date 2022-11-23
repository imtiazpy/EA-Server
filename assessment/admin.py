from django.contrib import admin

from .models import (
    Assessment,
    QuestionTopic,
    Result
)


admin.site.register(Assessment)
admin.site.register(QuestionTopic)
admin.site.register(Result)

