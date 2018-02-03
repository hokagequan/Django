from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os import path
from ..models import AppFile
import os

def get_all_packages():
	rel = list()
	pack_name = "packages"
	fs = FileSystemStorage()
	files = os.listdir(path.join(settings.MEDIA_ROOT, pack_name))

	for file in files:
		url = fs.url(path.join(pack_name, file))
		app_file = AppFile(name=file, url=url)
		rel.append(app_file)

	return rel