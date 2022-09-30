from django.contrib import admin

from .models import (
    Assessment,
    QuestionTopic,
    MCQuestion,
    Choice,
    TrueFalseQuestion,
    ShortAnswerQuestion,
    Answer
)


admin.site.register(Assessment)
admin.site.register(QuestionTopic)
admin.site.register(MCQuestion)
admin.site.register(Choice)
admin.site.register(TrueFalseQuestion)
admin.site.register(ShortAnswerQuestion)
admin.site.register(Answer)

