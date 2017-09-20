# thumbor_mongodb
Thumbor MongoDB loader with GridFS support

This project is based on https://github.com/timich/thumbor_mongodb which is no longer maintained and hasn't support for GridFS.
This is my first time programming in python, so any PRs are welcome :)

Wrok with tc_mongodb on https://github.com/thumbor-community/mongodb

```
LOADER = 'thumbor_mongodb.loader' #loader calling
MONGO_STORAGE_SERVER_HOST = '192.168.137.166' #host
MONGO_STORAGE_SERVER_PORT = '27017' #port
MONGO_STORAGE_SERVER_DB = 'picture' #MongoDB database name, inside it will be created collections fs.files and fs.chunks
MONGO_STORAGE_SERVER_COLLECTION = 'pic1' #MongoDB collection
```

Url should look like: http://thumbor-server.domain/unsafe/smart/1c6d2372252f4e18a54112a589017441

Upload by tc_mongodb `Location: /image/1c6d2372252f4e18a54112a589017441/image.ksh`
where `1c6d2372252f4e18a54112a589017441` is `path` of file saved in GridFS

