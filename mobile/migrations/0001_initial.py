# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('mobile_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('iso_alpha_2_code', self.gf('django.db.models.fields.CharField')(default='ZA', unique=True, max_length=2)),
        ))
        db.send_create_signal('mobile', ['Country'])

        # Adding model 'District'
        db.create_table('mobile_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Country'])),
        ))
        db.send_create_signal('mobile', ['District'])

        # Adding model 'Chief'
        db.create_table('mobile_chief', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.District'])),
        ))
        db.send_create_signal('mobile', ['Chief'])

        # Adding model 'Village'
        db.create_table('mobile_village', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('chief', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Chief'])),
        ))
        db.send_create_signal('mobile', ['Village'])

        # Adding model 'Submission'
        db.create_table('mobile_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submitted_by', to=orm['auth.User'])),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal('mobile', ['Submission'])

        # Adding model 'HealthPost'
        db.create_table('mobile_healthpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mobile', ['HealthPost'])

        # Adding model 'AgeRange'
        db.create_table('mobile_agerange', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('end', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('mobile', ['AgeRange'])

        # Adding model 'Person'
        db.create_table('mobile_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
        ))
        db.send_create_signal('mobile', ['Person'])

        # Adding model 'BirthForm'
        db.create_table('mobile_birthform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('father', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('mother', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.District'])),
            ('chief', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Chief'])),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Village'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person_birth', unique=True, to=orm['mobile.Person'])),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Submission'], unique=True)),
        ))
        db.send_create_signal('mobile', ['BirthForm'])

        # Adding model 'DeathForm'
        db.create_table('mobile_deathform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('death_description', self.gf('django.db.models.fields.TextField')()),
            ('age_range', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.AgeRange'])),
            ('health_post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.HealthPost'])),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Village'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person_death', unique=True, to=orm['mobile.Person'])),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Person'], unique=True)),
        ))
        db.send_create_signal('mobile', ['DeathForm'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('mobile_country')

        # Deleting model 'District'
        db.delete_table('mobile_district')

        # Deleting model 'Chief'
        db.delete_table('mobile_chief')

        # Deleting model 'Village'
        db.delete_table('mobile_village')

        # Deleting model 'Submission'
        db.delete_table('mobile_submission')

        # Deleting model 'HealthPost'
        db.delete_table('mobile_healthpost')

        # Deleting model 'AgeRange'
        db.delete_table('mobile_agerange')

        # Deleting model 'Person'
        db.delete_table('mobile_person')

        # Deleting model 'BirthForm'
        db.delete_table('mobile_birthform')

        # Deleting model 'DeathForm'
        db.delete_table('mobile_deathform')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mobile.agerange': {
            'Meta': {'object_name': 'AgeRange'},
            'end': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'mobile.birthform': {
            'Meta': {'ordering': "['birth_date']", 'object_name': 'BirthForm'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'chief': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Chief']"}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.District']"}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_birth'", 'unique': 'True', 'to': "orm['mobile.Person']"}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Submission']", 'unique': 'True'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Village']"})
        },
        'mobile.chief': {
            'Meta': {'ordering': "['name']", 'object_name': 'Chief'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'mobile.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_alpha_2_code': ('django.db.models.fields.CharField', [], {'default': "'ZA'", 'unique': 'True', 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mobile.deathform': {
            'Meta': {'ordering': "['death_date']", 'object_name': 'DeathForm'},
            'age_range': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.AgeRange']"}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_description': ('django.db.models.fields.TextField', [], {}),
            'health_post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.HealthPost']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_death'", 'unique': 'True', 'to': "orm['mobile.Person']"}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Person']", 'unique': 'True'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Village']"})
        },
        'mobile.district': {
            'Meta': {'ordering': "['name']", 'object_name': 'District'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'mobile.healthpost': {
            'Meta': {'object_name': 'HealthPost'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mobile.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mobile.submission': {
            'Meta': {'ordering': "['date_added']", 'object_name': 'Submission'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submitted_by'", 'to': "orm['auth.User']"})
        },
        'mobile.village': {
            'Meta': {'ordering': "['name']", 'object_name': 'Village'},
            'chief': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mobile.Chief']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['mobile']
