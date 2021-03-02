from dataclasses import dataclass
from typing import List


@dataclass
class Music:
    name: str
    artist: str


@dataclass
class Playlist:
    name: str
    musics: List[Music]
