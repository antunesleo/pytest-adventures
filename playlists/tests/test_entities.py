from playlists.tests.factories import MusicFactory, PlaylistFactory


class TestMusic:
    def test_has_name(self):
        music = MusicFactory(name="It never ends")
        assert music.name == "It never ends"

    def test_has_artist(self):
        music = MusicFactory(artist="Bring Me The Horizon")
        assert music.artist == "Bring Me The Horizon"


class TestPlaylist:
    def test_has_name(self):
        playlist = PlaylistFactory(name="Metalcore 2000s")
        assert playlist.name == "Metalcore 2000s"

    def test_has_musics(self):
        musics = [MusicFactory(), MusicFactory()]
        playlist = PlaylistFactory(musics=musics)
        assert playlist.musics == musics
