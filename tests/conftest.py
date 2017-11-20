
def pytest_configure(config):
    from gqlclans.logic import PapiRequestSession
    from tests.requestsnapshot import FileSnapshotStore, SnapshotAdapter
    s_adaptor = SnapshotAdapter(
        FileSnapshotStore(
            'tests/snapshots',
        )
    )

    PapiRequestSession.adapters['https://'] = s_adaptor


def pytest_unconfigure(config):
    from gqlclans.logic import PapiRequestSession
    del PapiRequestSession.adapters['https://']