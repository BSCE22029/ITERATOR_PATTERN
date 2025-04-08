from typing import List, Protocol

# Interface: SongIterator
class SongIterator(Protocol):
    def has_next(self) -> bool:
        ...

    def next(self):
        ...

# Class: Song
class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def get_info(self) -> str:
        return f"{self.title} by {self.artist}"

# Concrete Iterator
class ConcreteSongIterator(SongIterator):
    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.position = 0

    def has_next(self) -> bool:
        return self.position < len(self.songs)

    def next(self) -> Song:
        if not self.has_next():
            raise StopIteration("No more songs in the playlist.")
        song = self.songs[self.position]
        self.position += 1
        return song

# Interface: Playlist
class Playlist(Protocol):
    def create_iterator(self) -> SongIterator:
        ...

# Concrete Playlist
class ConcretePlaylist(Playlist):
    def __init__(self):
        self.songs: List[Song] = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def create_iterator(self) -> SongIterator:
        return ConcreteSongIterator(self.songs)

# Client
class Client:
    @staticmethod
    def main():
        playlist = ConcretePlaylist()
        playlist.add_song(Song("Let It Be", "The Beatles"))
        playlist.add_song(Song("Bohemian Rhapsody", "Queen"))
        playlist.add_song(Song("Imagine", "John Lennon"))

        iterator = playlist.create_iterator()

        while iterator.has_next():
            song = iterator.next()
            print(song.get_info())

# Run the client
if __name__ == "__main__":
    Client.main()
