from django import forms
from django.forms.formsets import formset_factory

from rockaway.construction.models import Assessment, StepType, WorkStep


class AssessmentForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)
    damage_assessment = forms.CharField(widget=forms.Textarea)
    permits_required = forms.BooleanField(required=False)
    permits = forms.CharField(widget=forms.Textarea, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)

    def save(self):
        assessment = Assessment()
        assessment.address = self.cleaned_data['address']
        assessment.damage_assessment = self.cleaned_data['damage_assessment']
        assessment.permits_required = self.cleaned_data['permits_required']
        assessment.permits = self.cleaned_data['permits']
        assessment.notes = self.cleaned_data['notes']
        assessment.save()
        return assessment


class BaseStepForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    scope = forms.ChoiceField(choices=WorkStep.SCOPES)
    time_required = forms.IntegerField()
    permit = forms.BooleanField(required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def save(self, assessment):
        obj = WorkStep()
        obj.assessment = assessment
        obj.work_type = StepType.objects.get(title=self.work_type)
        obj.scope = self.cleaned_data['scope']
        obj.description = self.cleaned_data['description']
        obj.permit_required = self.cleaned_data['permit']
        obj.time_required = self.cleaned_data['time_required']
        obj.start_date = self.cleaned_data['start_date']
        obj.end_date = self.cleaned_data['end_date']
        obj.progress = WorkStep.NEW
        obj.save()
        return obj


def form_factory(work, head=None):
    class f(BaseStepForm):
        heading = head
        prefix = work
        work_type = work
    return f

DemoBasementForm = form_factory('demo-basement', 'Basement')
DemoFirstForm = form_factory('demo-first', 'First Floor')
DemoSecondForm = form_factory('demo-second', 'Second Floor')
MoldBasementForm = form_factory('mold-basement', 'Basement')
MoldFirstForm = form_factory('mold-first', 'First Floor')
MoldSecondForm = form_factory('mold-second', 'Second Floor')
FoundationForm = form_factory('foundation', 'Foundation')
FramingForm = form_factory('framing', 'Framing')
PlumbingForm = form_factory('plumbing', 'Plumbing')
ElectricalForm = form_factory('electrical', 'Electrical')
HVACForm = form_factory('hvac', 'HVAC')
DrywallForm = form_factory('drywall', 'Drywall and Insulation')
CarpentryForm = form_factory('carpentry', 'Carpentry and Millwork')
FlooringForm = form_factory('flooring', 'Flooring')
PaintingForm = form_factory('painting', 'Painting')
