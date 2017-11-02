'''

Usage example

s = requests.Session()

s.mount('http://', SnapshotAdapter(FileSnapshotStore('snapshot.txt', True)))
result = s.get('http://google.com/')
'''

import warnings
import pickle
import hashlib
import os
import requests
from requests.adapters import BaseAdapter


class SnapshotException(Exception):
    pass


class FileSnapshotStore(object):
    store = None
    filepath = ''

    def __init__(self, filepath, write_snapshots=False):
        if write_snapshots:
            warnings.warn('Writing snapshots is enabled! It should be turns off after snapshots is created.')
        self.store = {}
        self.filepath = filepath
        self.write_snapshots = write_snapshots
        if os.path.isfile(filepath):
            self.store = pickle.load(open(filepath, 'rb'))
        elif not write_snapshots:
            raise SnapshotException('Cannot find snapshot file and write_snapshots option is set to False.')

    def get_data_for_request(self, request):
        return self.store.get(self.make_key_from_request(request))

    def make_snapshot(self, request, response):
        if not self.write_snapshots:
            raise SnapshotException('Writing snapshots is disabled.')

        self.store[self.make_key_from_request(request)] = response
        pickle.dump(self.store, open(self.filepath, 'wb'))

    @staticmethod
    def make_key_from_request(request):
        key_base = hashlib.md5()
        key_base.update(request.url.encode('utf-8'))
        key_base.update(request.method.encode('utf-8'))
        #key_base.update(str(request.body))
        return key_base.hexdigest()


class SnapshotAdapter(BaseAdapter):
    snapshots_store = None

    def __init__(self, snapshots_store):
        self.snapshots_store = snapshots_store

    def send(self, request, **kwargs):
        response = self.snapshots_store.get_data_for_request(request)

        if not response:
            warnings.warn('Trying to access url from tests. Url is {}'.format(request.url))
            my_session = requests.Session()
            response = my_session.send(request)
            self.snapshots_store.make_snapshot(request, response)

        return response
