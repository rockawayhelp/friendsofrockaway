from django import forms

from rockaway.construction import models


class AssessmentForm(forms.Form):
    creator = forms.IntegerField(widget=forms.HiddenInput)
    address = forms.TextField()

    def __new__(cls, *a, **kw):
        steps = models.StepType.objects.all()
        for s in steps:
            field_description = forms.TextField()
            field_time = forms.IntegerField(help='(%s)' % s.unit)
            field_start = forms.DateField()
            field_end = forms.DateField()
            setattr(cls, '%s_description' % s.title, field_description)
            setattr(cls, '%s_time' % s.title, field_time)
            setattr(cls, '%s_start' % s.title, field_start)
            setattr(cls, '%s_end' % s.title, field_end)
        return object.__new__(cls, *a, **kw)

    def save(self):
        assessment = models.Assessment.objects.create(
                creator=self.cleaned_data['creator'],
                address=self.cleaned_data['address'])

        steps = models.StepType.objects.all()
        for s in steps:
            description = self.cleaned_data.get('%s_description' % s.title)
            time = self.cleaned_data.get('%s_time' % s.title)
