from playlists.repositories import InMemoryPlaylistRepository
from playlists.tests.factories import PlaylistFactory


class TestInMemoryPlaylistRepository:
    def test_add(self):
        playlist = PlaylistFactory()
        repository = InMemoryPlaylistRepository()
        repository.add(playlist)
        assert playlist == repository.list()[0]

    def test_list(self):
        first_playlist = PlaylistFactory()
        second_playlist = PlaylistFactory()
        repository = InMemoryPlaylistRepository()
        repository.add(first_playlist)
        repository.add(second_playlist)

        playlists = repository.list()
        assert len(playlists) == 2
        assert [first_playlist, second_playlist] == playlists
