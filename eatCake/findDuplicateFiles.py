# << Swami Shreeji >>
# 8 Jan 2018

# You left your computer unlocked and your friend decided to troll you by copying
#  a lot of your files to random spots all over your file system.

# Even worse, she saved the duplicate files with random, embarrassing names 
# ("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).

# Write a function that returns a list of all the duplicate files. We'll 
# check them by hand before actually deleting them, since programmatically 
# deleting files is really scary. To help us confirm that two files are actually 
# duplicates, return a list of tuples where:

# the first item is the duplicate file
# the second item is the original file
# For example:

#   [('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
#  ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
# You can assume each file was only duplicated once.

# My solution is largely modeled after an optimized solution on stackoverflow. https://goo.gl/TC6dqY

import sys
import os
import hashlib

def chunkReader(fobj, chunkSize = 1024): 
	''' A generator that reads a file in chunks of bytes '''
	while True:
		chunk = fobj.read(chunkSize)
		if not chunk:
			return
		yield chunk

def getHash(filename, firstChunkOnly = False, hash = hashlib.sha1):
	hashObj = hash()
	fileObject = open(filename, 'rb')

	if firstChunkOnly:
		hashObj.update(fileObject.read(1024))
	else:
		for chunk in chunkReader(fileObject):
			hashObj.update(chunk)
	hashed = hashObj.digest()

	fileObject.close()
	return hashed

def checkForDups(paths, hash = hashlib.sha1):
	hashesBySize = {}
	hashesOn1k = {}
	hashesFull = {}

	formatAnswer = []

	for path in paths:
		for dirpath, dirnames, filenames in os.walk(path):
			for filename in filenames:
				fullPath = os.path.join(dirpath, filename)
				try:
					fileSize = os.path.getsize(fullPath)
				except (OSError,):
					# Not accessible (permissions etc)
					pass

				duplicate = hashesBySize.get(fileSize)
				
				if duplicate:
					hashesBySize[fileSize].append(fullPath)
				else:
					hashesBySize[fileSize] = []
					hashesBySize[fileSize].append(fullPath)

	# For all files that have the same file size, get their hashes on the 1st 1024 bytes
	for __, files in hashesBySize.items():
		# The case when we have a unique file
		if len(files) < 2:
			continue

		for filename in files:
			smallHash = getHash(filename, firstChunkOnly = True)

			duplicate = hashesOn1k.get(smallHash)
			if duplicate:
				hashesOn1k[smallHash].append(filename)
			else:
				hashesOn1k[smallHash] = []
				hashesOn1k[smallHash].append(filename)

	# For the files we hashed the 1st 1024 bytes of, get their hash on the full size. If collision, then dups
	for __, files in hashesOn1k.items():
		# Unique hash
		if len(files) < 2:
			continue

		for filename in files:
			fullHash = getHash(filename, firstChunkOnly = False)

			duplicate = hashesFull.get(fullHash)
			if duplicate:
				# print "We found a duplicate! Duplicate:Original -- %s and %s" % (duplicate, filename)
				formatAnswer.append( (duplicate, filename) )
			else:
				hashesFull[fullHash] = filename

	print formatAnswer

if sys.argv[1:]:
	checkForDups(sys.argv[1:])
else:
	print "Pass the paths to check as cmd line args to this script"
