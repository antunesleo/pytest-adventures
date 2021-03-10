from uuid import uuid4

import factory

from playlists.entities import Music, Playlist


class MusicFactory(factory.Factory):
    class Meta:
        model = Music

    id = uuid4()
    name = "It was written in blood"
    artist = "Bring Me The Horizon"


class PlaylistFactory(factory.Factory):
    class Meta:
        model = Playlist

    id = uuid4()
    name = "Metalcore 10s"
    musics = factory.List([factory.SubFactory(MusicFactory) for _ in range(5)])
