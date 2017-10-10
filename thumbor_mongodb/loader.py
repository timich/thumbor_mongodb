#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

from tornado.concurrent import return_future
from pymongo import MongoClient
from bson.objectid import ObjectId
import gridfs

def __conn__(self):
	connection = MongoClient(
		self.config.MONGO_STORAGE_SERVER_HOST,
		self.config.MONGO_STORAGE_SERVER_PORT,
		readPreference=self.config.MONGO_STORAGE_READ_PREFERENCE
	)

	db = connection[self.config.MONGO_STORAGE_SERVER_DB]
	return db

@return_future
def load(self, path, callback):
	db = __conn__(self)
	fs = gridfs.GridFS(db)
	contents = fs.get(ObjectId(path)).read()
	callback(contents)
