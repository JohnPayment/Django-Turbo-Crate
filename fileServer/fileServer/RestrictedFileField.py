from django.forms import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy

class RestrictedFileField(FileField):

	def __init__(self, *args, **kwargs):
		self.maxUploadSize = kwargs.pop("max_upload_size")

		super(RestrictedFileField, self).__init__(*args, **kwargs)

	def clean(self, *args, **kwargs):
		data = super(RestrictedFileField, self).clean(*args, **kwargs)

		try:
			if data.size > self.maxUploadSize:
				raise forms.ValidationError(ugettext_lazy('Please keep filesize under %s. Current filesize %s') % (self.maxUploadSize, data.size))
		except AttributeError:
			pass

		return data
