import pytest

from playlists.repositories import (
    InMemoryPlaylistRepository,
    PlaylistRepository,
    MusicRepository,
    InMemoryMusicRepository,
)
from playlists.tests.factories import MusicFactory, PlaylistFactory
from playlists.usecases import create_playlist, add_music_to_playlist


@pytest.fixture
def playlist_repository() -> PlaylistRepository:
    return InMemoryPlaylistRepository()


@pytest.fixture
def music_repository() -> MusicRepository:
    return InMemoryMusicRepository()


class TestCreatePlaylist:
    def test_should_create(self, playlist_repository: PlaylistRepository):
        playlist = create_playlist("Metalcore 10s", playlist_repository)
        created_playlist = playlist_repository.get(playlist.id)
        assert playlist.id == created_playlist.id
        assert playlist.name == created_playlist.name


class TestAddMusicToPlaylist:
    def test_add_music_to_playlist(
        self, music_repository: MusicRepository, playlist_repository: PlaylistRepository
    ):
        music = MusicFactory()
        music_repository.add(music)
        playlist = PlaylistFactory()
        playlist_repository.add(playlist)

        updated_playlist = add_music_to_playlist(
            music.id, playlist.id, music_repository, playlist_repository
        )
        assert updated_playlist
        assert playlist.id == updated_playlist.id
        assert playlist.musics[0] == updated_playlist.musics[0]
        updated_playlist_from_repo = playlist_repository.get(playlist.id)
        assert updated_playlist_from_repo
        assert playlist.musics[0] == updated_playlist_from_repo.musics[0]
