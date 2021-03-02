import factory

from playlists.entities import Music, Playlist


class MusicFactory(factory.Factory):
    class Meta:
        model = Music

    name = "It was written in blood"
    artist = "Bring Me The Horizon"


class PlaylistFactory(factory.Factory):
    class Meta:
        model = Playlist

    name = "Metalcore 2000s"
    musics = factory.List([factory.SubFactory(MusicFactory) for _ in range(5)])
