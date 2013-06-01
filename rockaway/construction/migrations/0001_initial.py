# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Assessment'
        db.create_table(u'construction_assessment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('damage_assessment', self.gf('django.db.models.fields.TextField')()),
            ('permits_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permits', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'construction', ['Assessment'])

        # Adding model 'StepType'
        db.create_table(u'construction_steptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('skilled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'construction', ['StepType'])

        # Adding model 'WorkStep'
        db.create_table(u'construction_workstep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assessment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['construction.Assessment'])),
            ('work_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['construction.StepType'])),
            ('scope', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('time_required', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('progress', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'construction', ['WorkStep'])


    def backwards(self, orm):
        # Deleting model 'Assessment'
        db.delete_table(u'construction_assessment')

        # Deleting model 'StepType'
        db.delete_table(u'construction_steptype')

        # Deleting model 'WorkStep'
        db.delete_table(u'construction_workstep')


    models = {
        u'construction.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'damage_assessment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'permits': ('django.db.models.fields.TextField', [], {}),
            'permits_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'construction.steptype': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'StepType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'construction.workstep': {
            'Meta': {'object_name': 'WorkStep'},
            'assessment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['construction.Assessment']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'scope': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_required': ('django.db.models.fields.IntegerField', [], {}),
            'work_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['construction.StepType']"})
        }
    }

    complete_apps = ['construction']