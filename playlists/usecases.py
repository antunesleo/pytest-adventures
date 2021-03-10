from uuid import UUID

from playlists.entities import Playlist
from playlists.repositories import PlaylistRepository, MusicRepository


def create_playlist(name: str, playlist_repository: PlaylistRepository) -> Playlist:
    object_id = playlist_repository.object_id()
    playlist = Playlist(object_id, name)
    playlist_repository.add(playlist)
    return playlist


def add_music_to_playlist(
    music_id: UUID,
    playlist_id: UUID,
    music_repository: MusicRepository,
    playlist_repository: PlaylistRepository,
):
    music = music_repository.get(music_id)
    playlist = playlist_repository.get(playlist_id)
    playlist.add_music(music)
    playlist_repository.update(playlist)
    return playlist
