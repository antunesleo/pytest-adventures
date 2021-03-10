from typing import List
from uuid import UUID


class Music:
    def __init__(self, id: UUID, name: str, artist: str):
        self.id = id
        self.name = name
        self.artist = artist


class Playlist:
    def __init__(self, id: UUID, name: str, musics: List[Music] = None):
        self.id = id
        self.name = name
        self.musics = musics or []

    def add_music(self, music: Music):
        self.musics.append(music)
