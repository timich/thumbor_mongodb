easy_install /usr/src/app/thumbor_mongodb/
mv /usr/src/app/thumbor_mongodb/thumbor_mongodb /usr/local/lib/python2.7/site-packages/
cp /usr/local/lib/python2.7/site-packages/tc_mongodb/storages/mongo_storage.py /usr/local/lib/python2.7/site-packages/thumbor/storages/mongo_storage.py
return 0