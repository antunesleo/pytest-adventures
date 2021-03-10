from uuid import UUID

from playlists.tests.factories import MusicFactory, PlaylistFactory


class TestMusic:
    def test_has_name(self):
        music = MusicFactory(name="It never ends")
        assert music.name == "It never ends"

    def test_has_artist(self):
        music = MusicFactory(artist="Bring Me The Horizon")
        assert music.artist == "Bring Me The Horizon"


class TestPlaylist:
    def test_has_id(self):
        playlist = PlaylistFactory(name="Metalcore 2000s")
        assert isinstance(playlist.id, UUID)

    def test_has_name(self):
        playlist = PlaylistFactory(name="Metalcore 2000s")
        assert playlist.name == "Metalcore 2000s"

    def test_has_musics(self):
        musics = [MusicFactory(), MusicFactory()]
        playlist = PlaylistFactory(musics=musics)
        assert playlist.musics == musics

    def test_should_add_music(self):
        playlist = PlaylistFactory(musics=[])
        music = MusicFactory(name="It never ends")
        playlist.add_music(music)
        assert len(playlist.musics) == 1
        assert playlist.musics[0].id == music.id
        assert playlist.musics[0].name == music.name
