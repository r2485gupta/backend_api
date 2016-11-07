from django.db import models
from django.contrib.auth.models import User


class user_details(models.Model):
	user_id = models.ForeignKey(User)
	short_bio = models.CharField(max_length=1000)
	twitter_handle = models.CharField(max_length=255)
	facebook_url = models.CharField(max_length=255)
	linkedin_url = models.CharField(max_length=255)
	googleplus_url = models.CharField(max_length=255)
	dob = models.DateField()
	city = models.CharField(max_length=255)
	photo = models.FilePathField()\
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class education(models.Model):
	user_id = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	education_type = models.CharField(max_length=255)
	institution_name = models.CharField(max_length=255)
	aggregate = models.IntegerField()
	document = models.FilePathField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class work(models.Model):
	user_id = models.ForeignKey(User)
	work_type = models.CharField(max_length=255)
	internship_company_name = models.CharField(max_length=255)
	internship_date_from = models.DateField()
	internship_date_to = models.DateField()
	internship_title = models.CharField()
	internship_status = models.CharField(max_length=255)
	internship_document = models.FilePathField()
	job_date_from = models.DateField()
	job_date_to = models.DateField()
	job_company_name = models.CharField(max_length=255)
	job_designation = models.CharField(max_length=255)
	job_document = models.FilePathField()
	freelancer_client_name = models.CharField(max_length=255)
	freelancer_project_title = models.CharField(max_length=255)
	freelancer_link = models.CharField(max_length=255)
	freelancer_status = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class certification(models.Model):
	user_id = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	agency = models.CharField(max_length=255)
	mode_of_certification = models.CharField(max_length=255)
	details = models.CharField(max_length=1000)
	document = models.FilePathField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class publication(models.Model):
	user_id = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	mode = models.CharField(max_length=255)
	journal = models.CharField(max_length=1000)
	details = models.CharField(max_length=1000)
	status = models.CharField(max_length=255)
	link = models.CharField(max_lenght=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class extracurricular_activities(models.Model):
	user_id = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	activity_type = models.CharField(max_length=255)
	activity_details = models.CharField(max_length=1000, default='none')
	title = models.CharField(max_length=255)
	organization = models.CharField(max_length=255)
	organization_details = models.CharField(max_length=1000)
	link = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class patent(models.Model):
	user_id = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	mode = models.CharField(max_length=255)
	patent_details = models.CharField(max_length=255)
	patent_status = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class achievements(models.Model):
	user_id = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	achievement_type = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	organization = models.CharField(max_length=255)
	details = models.CharField(max_length=1000)
	link = models.CharField(max_length=255)
	document = models.FilePathField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class skills(models.Model):
	user_id = models.ForeignKey(User)
	technical_skills = models.CharField(max_length=1000)
	soft_skills = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class languages(models.Model):
	user_id = models.ForeignKey(User)
	language_name = models.CharField(max_length=255)
	fluency = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
