from django.core.management.base import BaseCommand

from rockaway.construction.models import StepType


class Command(BaseCommand):

    def handle(self, *a, **kw):
        steptypes = (
            ('demo-basement', StepType.DAYS, False),
            ('demo-first', StepType.DAYS, False),
            ('demo-second', StepType.DAYS, False),
            ('mold-basement', StepType.HOURS, True),
            ('mold-first', StepType.HOURS, True),
            ('mold-second', StepType.HOURS, True),
            ('foundation', StepType.HOURS, True),
            ('framing', StepType.HOURS, True),
            ('plumbing', StepType.HOURS, True),
            ('electrical', StepType.HOURS, True),
            ('hvac', StepType.HOURS, True),
            ('drywall', StepType.DAYS, False),
            ('carpentry', StepType.DAYS, False),
            ('flooring', StepType.DAYS, False),
            ('painting', StepType.DAYS, False),
        )

        for t, u, s in steptypes:
            StepType.objects.create(
                title=t,
                unit=u,
                skilled=s)
