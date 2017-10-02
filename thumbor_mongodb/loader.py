#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

import gridfs
from pymongo import MongoClient
from tornado.concurrent import return_future
from datetime import datetime, timedelta


def __conn__(self):
    connection = MongoClient(
        self.config.MONGO_STORAGE_SERVER_HOST,
        self.config.MONGO_STORAGE_SERVER_PORT,
        readPreference='primaryPreferred'
    )
    db = connection[self.config.MONGO_STORAGE_SERVER_DB]
    storage = db[self.config.MONGO_STORAGE_SERVER_COLLECTION]
    return connection, db, storage

def __is_expired(self, stored):
    timediff = datetime.now() - stored.get('created_at')
    return timediff > timedelta(seconds=self.config.STORAGE_EXPIRATION_SECONDS)

@return_future
def load(self, path, callback):
    connection, db, storage = __conn__(self)
    stored = storage.find_one({'path': path})


    if not stored or __is_expired(self,stored):
        callback(None)
        return
    fs = gridfs.GridFS(db)
    contents = fs.get(stored['file_id']).read()
    callback(str(contents))


