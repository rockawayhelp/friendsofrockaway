# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StepType.slug'
        db.add_column(u'construction_steptype', 'slug',
                      self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StepType.slug'
        db.delete_column(u'construction_steptype', 'slug')


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
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
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
            'permit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'scope': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_required': ('django.db.models.fields.IntegerField', [], {}),
            'work_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['construction.StepType']"})
        }
    }

    complete_apps = ['construction']