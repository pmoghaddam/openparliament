# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Hansard.wordcloud'
        db.add_column('hansards_hansard', 'wordcloud', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Hansard.wordcloud'
        db.delete_column('hansards_hansard', 'wordcloud')


    models = {
        'bills.bill': {
            'Meta': {'ordering': "('number_only',)", 'object_name': 'Bill'},
            'added': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'law': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'legisinfo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'number_only': ('django.db.models.fields.SmallIntegerField', [], {}),
            'privatemember': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Session']", 'symmetrical': 'False'}),
            'sponsor_member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ElectedMember']", 'null': 'True', 'blank': 'True'}),
            'sponsor_politician': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Politician']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'core.electedmember': {
            'Meta': {'object_name': 'ElectedMember'},
            'end_date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Party']"}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Politician']"}),
            'riding': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Riding']"}),
            'sessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Session']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        },
        'core.party': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Party'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        'core.politician': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Politician'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_family': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name_given': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'parlpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'blank': 'True'})
        },
        'core.riding': {
            'Meta': {'ordering': "('province', 'name')", 'object_name': 'Riding'},
            'edid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'})
        },
        'core.session': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Session'},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parliamentnum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sessnum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'hansards.hansard': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Hansard'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Session']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'wordcloud': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wordoftheday': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'hansards.hansardcache': {
            'Meta': {'object_name': 'HansardCache'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hansard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hansards.Hansard']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hansards.statement': {
            'Meta': {'ordering': "('sequence',)", 'object_name': 'Statement'},
            'bills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bills.Bill']", 'symmetrical': 'False', 'blank': 'True'}),
            'hansard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hansards.Hansard']"}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '110', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ElectedMember']", 'null': 'True', 'blank': 'True'}),
            'mentioned_politicians': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'statements_with_mentions'", 'blank': 'True', 'to': "orm['core.Politician']"}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Politician']", 'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'speaker': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'wordcount': ('django.db.models.fields.IntegerField', [], {}),
            'written_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['hansards']
