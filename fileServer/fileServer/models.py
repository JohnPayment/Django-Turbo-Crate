from django.db import models

def setDirectory(instance, filename):
	return '{0}/{1}'.format(instance.username, filename)

class Document(models.Model):
	username = "guest"
	docfile = models.FileField(upload_to=setDirectory)
