
def pytest_configure(config):
    from logic import PapiRequestSession
    from requestsnapshot import FileSnapshotStore, SnapshotAdapter

    s_adaptor = SnapshotAdapter(
        FileSnapshotStore(
            'testsnapshots.txt',
            write_snapshots=True
        )
    )

    PapiRequestSession.adapters['https://'] = s_adaptor

def pytest_unconfigure(config):
    from logic import PapiRequestSession
    del PapiRequestSession.adapters['https://']