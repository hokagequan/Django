from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os import path
from ..models import AppFile
import os

def get_files(folder):
	rel = list()
	fs = FileSystemStorage()
	files = os.listdir(path.join(settings.MEDIA_ROOT, folder))

	for file in files:
		url = fs.url(path.join(folder, file))
		app_file = AppFile(name=file, url=url)
		rel.append(app_file)

	return rel

def get_all_packages():
	get_files("packages")

def get_all_setups():
	get_files("setups")