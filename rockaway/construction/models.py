from datetime import datetime

from django.conf import settings
from django.db import models


class Assessment(models.Model):
    address = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    damage_assessment = models.TextField()
    permits_required = models.BooleanField()
    permits = models.TextField()
    notes = models.TextField()

    def __unicode__(self):
        return self.address


class StepType(models.Model):
    HOURS = 'hours'
    DAYS = 'days'
    UNITS = (
        (HOURS, 'Hours'),
        (DAYS, 'Days'),
    )

    slug = models.CharField(max_length=255, unique=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    weight = models.IntegerField(default=1)
    unit = models.CharField(max_length=16, choices=UNITS)
    skilled = models.BooleanField(default=False)

    class Meta(object):
        ordering = ('weight',)

    def __unicode__(self):
        return self.title


class WorkStep(models.Model):
    NEW = 'new'
    STARTED = 'started'
    FINISHED = 'finished'
    PROGRESS = (
        (NEW, 'New'),
        (STARTED, 'Started'),
        (FINISHED, 'Finished'),
    )

    NO_WORK = 'no-work'
    ROUGH_IN = 'rough-in'
    FINISHING = 'finishing'
    SCOPES = (
        (NO_WORK, 'No work required'),
        (ROUGH_IN, 'Rough-in'),
        (FINISHING, 'Finishing'),
    )

    assessment = models.ForeignKey(Assessment)
    work_type = models.ForeignKey(StepType)
    scope = models.CharField(max_length=16, choices=SCOPES)
    description = models.TextField()
    time_required = models.IntegerField()
    permit = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    progress = models.CharField(max_length=16, choices=PROGRESS)

    def __unicode__(self):
        s = (self.assessment, self.work_type, self.work_type.unit,
             self.time_required)
        return '%s: %s (%s %s)' % s
