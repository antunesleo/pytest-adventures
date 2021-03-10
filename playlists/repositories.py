from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4, UUID

from playlists.entities import Playlist, Music


class MusicRepository(ABC):
    @abstractmethod
    def object_id(self) -> UUID:
        pass

    @abstractmethod
    def add(self, music: Music):
        pass

    @abstractmethod
    def get(self, music_id: UUID) -> Music:
        pass

    @abstractmethod
    def update(self, music: Music):
        pass


class PlaylistRepository(ABC):
    @abstractmethod
    def object_id(self) -> UUID:
        pass

    @abstractmethod
    def get(self, playlist_id: UUID):
        pass

    @abstractmethod
    def list(self) -> List[Playlist]:
        pass

    @abstractmethod
    def add(self, playlist: Playlist):
        pass

    @abstractmethod
    def update(self, playlist: Playlist):
        pass


class InMemoryRepositoryMixin:
    def __init__(self):
        self._objects = []

    def get(self, object_id):
        for _object in self._objects:
            if _object.id == object_id:
                return _object
        raise Exception

    def update(self, object_to_up):
        for index, _object in enumerate(self._objects):
            if _object.id == object_to_up.id:
                self._objects[index] = object_to_up
                return
        raise Exception

    def object_id(self) -> UUID:
        return uuid4()

    def list(self) -> List:
        return self._objects

    def add(self, new_object):
        self._objects.append(new_object)


class InMemoryMusicRepository(InMemoryRepositoryMixin, MusicRepository):
    pass


class InMemoryPlaylistRepository(InMemoryRepositoryMixin, PlaylistRepository):
    pass
