# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table('people_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthday_date', self.gf('django.db.models.fields.DateField')()),
            ('student_id_card', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=0)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups', to=orm['groups.Group'])),
        ))
        db.send_create_signal('people', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table('people_student')


    models = {
        'groups.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'senior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'students'", 'null': 'True', 'to': "orm['people.Student']"})
        },
        'people.student': {
            'Meta': {'object_name': 'Student'},
            'birthday_date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': "orm['groups.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'student_id_card': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '0'})
        }
    }

    complete_apps = ['people']