from django.contrib import admin

from rockaway.construction.models import Assessment, StepType, WorkStep


class InlineStepAdmin(admin.StackedInline):
    extra = 0
    model = WorkStep


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [InlineStepAdmin]


admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(StepType)
admin.site.register(WorkStep)
