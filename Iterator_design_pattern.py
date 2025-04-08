from typing import List

class SongIterator:
    def has_next(self) -> bool:
        pass # just an abstract method

    def next(self):
        pass # just an abstract method

class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def get_info(self) -> str:
        return f"{self.title} by {self.artist}"

class ConcreteSongIterator(SongIterator):   # implementing the SongIterator class
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

class Playlist:
    def create_iterator(self) -> SongIterator:
        pass # just an abstract method

class ConcretePlaylist(Playlist):   # implementing the Playlist class
    def __init__(self):
        self.songs: List[Song] = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def create_iterator(self) -> SongIterator:
        return ConcreteSongIterator(self.songs)

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

if __name__ == "__main__":
    Client.main()
