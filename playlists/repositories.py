from abc import ABC, abstractmethod
from typing import List

from playlists.entities import Playlist


class PlaylistRepository(ABC):
    @abstractmethod
    def list(self) -> List[Playlist]:
        pass

    @abstractmethod
    def add(self, playlist: Playlist):
        pass


class InMemoryPlaylistRepository(PlaylistRepository):
    def __init__(self):
        self._playlists = []

    def list(self) -> List[PlaylistRepository]:
        return self._playlists

    def add(self, playlist: Playlist):
        self._playlists.append(playlist)
