from django import forms
from fileServer.RestrictedFileField import RestrictedFileField

#In Bytes
MAX_FILE_SIZE = 104857600

class DocumentForm(forms.Form):
	docfile = RestrictedFileField(label='Select a file', max_upload_size=MAX_FILE_SIZE)

	def clean(self):
		cleaned_data = self.cleaned_data
		return cleaned_data
