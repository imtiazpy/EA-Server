from django.contrib import admin

from .models import (
    Assessment,
    QuestionTopic,
    Question,
    QuestionSet,
    ChoiceSet,
    Choice
)

admin.site.register(Assessment)
admin.site.register(QuestionTopic)
admin.site.register(Question)
admin.site.register(QuestionSet)
admin.site.register(ChoiceSet)
admin.site.register(Choice)


