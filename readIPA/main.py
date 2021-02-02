import os
import re
import zipfile
import datetime
# import plistlib  # python 3.4+
from biplist import *

ipaFile = '/Users/m5pro/Documents/build/testipa/test.ipa'
zipFile = '/Users/m5pro/Documents/build/testipa/ipa.zip'
unzipPath = '/Users/m5pro/Documents/build/testipa/ipa'
outputIpaFile = '/Users/m5pro/Documents/build/testipa/test_{0}.ipa'

unzipIpaPath = '/Users/m5pro/Documents/build/testipa/ipa'


def unzip(inputPath, outputPath):
	zip_file = zipfile.ZipFile(inputPath)
	zip_list = zip_file.namelist()

	for f in zip_list:
		zip_file.extract(f, outputPath)

	zip_file.close()


def zipDir(inputPath, outputPath):
	zip_file = zipfile.ZipFile(outputPath, "w", zipfile.ZIP_DEFLATED)
	for path, dirnames, filenames in os.walk(inputPath):
		fpath = path.replace(inputPath, '')
		for filename in filenames:
			zip_file.write(os.path.join(path, filename), os.path.join(fpath, filename))

	zip_file.close()


def getIpaPlist(ipa_path, unzipPath):
	zip_file = zipfile.ZipFile(ipa_path)
	zip_list = zip_file.namelist()
	plist_file = find_plist_path(zip_list)
	for f in zip_list:
		zip_file.extract(f, unzipPath)
	zip_file.close()

	# return plistlib.loads(zip_file.read(plist_file))  # python 3.4+
	plist_path = os.path.join(unzipPath, plist_file)
	return readPlist(plist_path), plist_path  # python 2.7


def find_plist_path(name_list):
	pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
	for path in name_list:
		m = pattern.match(path)
		if m is not None:
			return m.group()


def print_ipa_info(plist_dict, plist_path):
	plist_dict['CFBundleIdentifier'] = 'com.test.ipa'
	writePlist(plist_dict, plist_path)
	print ('Display Name: %s' % plist_dict['CFBundleDisplayName'])
	print ('Bundle Identifier: %s' % plist_dict['CFBundleIdentifier'])
	print ('Version: %s' % plist_dict['CFBundleShortVersionString'])


# unzip(ipaFile, unzipPath)
plist_dict, plist_path = getIpaPlist(ipaFile, unzipPath)
print_ipa_info(plist_dict, plist_path)
zipDir(unzipPath, zipFile)
os.rename(zipFile, outputIpaFile.format(datetime.datetime.now().strftime('%Y%m%d%H%M')))
