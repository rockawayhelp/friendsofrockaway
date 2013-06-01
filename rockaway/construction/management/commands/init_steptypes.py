from django.core.management.base import BaseCommand

from rockaway.construction.models import StepType


class Command(BaseCommand):

    def handle(self, *a, **kw):
        steptypes = (
            ('demo-basement', 'Demolition (Basement)', StepType.DAYS, False),
            ('demo-first', 'Demolition (First)', StepType.DAYS, False),
            ('demo-second', 'Demolition (Second)', StepType.DAYS, False),
            ('mold-basement', 'Mold (Basement)', StepType.HOURS, True),
            ('mold-first', 'Mold (First)', StepType.HOURS, True),
            ('mold-second', 'Mold (Second)', StepType.HOURS, True),
            ('foundation', 'Foundation', StepType.HOURS, True),
            ('framing', 'Framing', StepType.HOURS, True),
            ('plumbing', 'Plumbing', StepType.HOURS, True),
            ('electrical', 'Electrical', StepType.HOURS, True),
            ('hvac', 'HVAC', StepType.HOURS, True),
            ('drywall', 'Drywall', StepType.DAYS, False),
            ('carpentry', 'Carpentry', StepType.DAYS, False),
            ('flooring', 'Flooring', StepType.DAYS, False),
            ('painting', 'Painting', StepType.DAYS, False),
        )

        for i, (l, t, u, s) in enumerate(steptypes):
            StepType.objects.create(
                slug=l,
                title=t,
                weight=i,
                unit=u,
                skilled=s)
