# thumbor_mongodb
Thumbor MongoDB loader with GridFS support

This project is based on https://github.com/dhardy92/thumbor_mongodb which is no longer maintained and hasn't support for GridFS.
This is my first time programming in python, so any PRs are welcome :)

```
LOADER = 'thumbor_mongodb.loader' #loader calling
MONGO_STORAGE_SERVER_HOST = 'localhost' #host
MONGO_STORAGE_SERVER_PORT = 27017 #port
MONGO_STORAGE_READ_PREFERENCE = 'primaryPreferred' #for from slave in replicaSet put there 'secondaryPreferred'
MONGO_STORAGE_SERVER_DB = 'images' #MongoDB database name, inside it will be created collections fs.files and fs.chunks
```

Url should look like: https://thumbor-server.domain/secret/fit-in/400x400/5756fcdd7d75bb07c378d9e7
where `5756fcdd7d75bb07c378d9e7` is `_id` of file saved in GridFS

Tested on Ubuntu 16.04 with:
- Thumbor 6.0.1
- MongoDB 3.2.7
- PyMongo 3.2.2
