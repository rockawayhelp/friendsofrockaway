from django.shortcuts import get_object_or_404, render
from rockaway.construction.models import Assessment, WorkStep
from rockaway.construction.forms import *


def assess(request):
    forms = [
        {'heading': 'Damage Assessment',
         'forms': [AssessmentForm()],},
        {'heading': 'Demolition Plan',
         'forms': [DemoBasementForm(),
                   DemoFirstForm(),
                   DemoSecondForm()],},
        {'heading': 'Mold Remediation',
         'forms': [MoldBasementForm(),
                   MoldFirstForm(),
                   MoldSecondForm()],},
        {'heading': 'Rough In',
         'forms': [FoundationForm(),
                   FramingForm(),
                   PlumbingForm(),
                   ElectricalForm(),
                   HVACForm()],},
        {'heading': 'Finishing',
         'forms': [DrywallForm(),
                   CarpentryForm(),
                   FlooringForm(),
                   PaintingForm()],}
    ]

    if request.method == 'POST':
        assessment_form = AssessmentForm(request.POST)
        valid = True
        for g in forms:
            for i, f in enumerate(g['forms']):
                g['forms'][i] = f.__class__(request.POST)
                if not g['forms'][i].is_valid():
                    valid = False
        if valid:
            assessment = forms[0]['forms'][0].save()
            for g in forms[1:]:
                for f in g['forms']:
                    f.save(assessment)
            return render(request, 'construction/done.html')

    return render(request, 'construction/assess.html', {'forms': forms})


def assessment_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'construction/assessment_list.html',
                  {'assessments': assessments})


def detail(request, assessment_id):
    assessment = get_object_or_404(Assessment, pk=assessment_id)
    return render(request, 'construction/detail.html',
                  {'assessment': assessment})
