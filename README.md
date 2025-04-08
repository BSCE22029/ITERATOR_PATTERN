
# Playlist Iterator - Python Implementation

This project demonstrates the **Iterator Design Pattern** using a music playlist as an example. It separates the logic of traversing a list of songs from the underlying playlist structure, enabling clean and extensible code.

---

## What is the Iterator Pattern?

The **Iterator Pattern** allows sequential access to elements of a collection without exposing its internal structure. It promotes separation of concerns and enhances flexibility by isolating iteration logic.

---

## Project Structure

```
playlist_iterator/
│
├── main.py              # Entry point for the program (Client)
├── song.py              # Song class definition
├── iterator.py          # SongIterator interface and ConcreteSongIterator class
├── playlist.py          # Playlist interface and ConcretePlaylist class
└── README.md            # Project documentation
```

---

## How It Works

- `Song` – A simple class that holds song information (title and artist).
- `SongIterator` – An interface that defines how to iterate through songs.
- `ConcreteSongIterator` – Implements the actual logic for traversing a list of songs.
- `Playlist` – An interface that exposes a `create_iterator()` method.
- `ConcretePlaylist` – Stores songs and returns an iterator for them.
- `Client` – Creates a playlist, adds songs, and uses the iterator to display each song.

---

## Getting Started

### Prerequisites

Make sure you have Python 3 installed on your system.

### Run the Project

```bash
python main.py
```

### Sample Output

```
Let It Be by The Beatles
Bohemian Rhapsody by Queen
Imagine by John Lennon
```

---

## Benefits of This Pattern

- **Encapsulation**: Keeps the internal playlist structure hidden from users.
- **Extensibility**: You can easily implement other iterators (e.g., reverse, shuffle).
- **Reusability**: Iterator logic can be reused across different types of collections.

---

## 👨‍💻 Author

**Muhammad Miqdad Ahmad**
**Muhammad Moiz Ahmad**


