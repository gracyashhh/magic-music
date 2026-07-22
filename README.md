# 🎵 Magic Music

A fast, lightweight, offline desktop music player built with **Python** and **Eel**.

Magic Music started as a personal project to learn Python and desktop app development. Over time it has grown into a feature-rich local music player with automatic album artwork, playlists, shuffle, repeat, and much more.

> **Mission:** Create a beautiful, completely free desktop music player that anyone can use without ads or subscriptions.

---

# ✨ Features

- 🎵 Play local MP3 files
- 🖼️ Automatically fetch album artwork from Spotify
- ⏯️ Play / Pause / Next / Previous
- 🔀 Shuffle mode
- 🔁 Repeat mode
- 🔊 Volume control
- ⏱️ Progress bar & seeking
- 📂 Automatically loads songs from the music folder
- 💻 Desktop interface built using HTML, CSS, JavaScript and Python

---

# 📷 Screenshots

*Coming soon*

---

# 🛠️ Built With

- Python
- Eel
- HTML
- CSS
- JavaScript
- pygame
- MoviePy
- Requests
- Spotify Web API
- python-dotenv

---

# 📁 Project Structure

```text
Magic Music/
│
├── getting-started-with-eel/
│   ├── music-player.py
│   ├── cover_art.py
│   ├── web/
│   └── MagicMusicSongs/
│
├── .env
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/gracyashhh/magic-music.git
cd magic-music
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

Run the application

```bash
python getting-started-with-eel/music-player.py
```

---

# 🎵 Adding Music

Copy your MP3 files into

```text
getting-started-with-eel/
    MagicMusicSongs/
```

The application automatically loads every supported song inside this folder.

---

# ⚠️ Known Issues

- Empty music folder currently causes an error (planned fix).
- Album artwork depends on Spotify search results.
- Some uncommon audio formats may require conversion before playback.

---

# 🗺️ Roadmap

## Version 1.0

- [ ] Handle empty music folder gracefully
- [ ] Better error messages
- [ ] Improve loading speed
- [ ] Better Spotify search matching
- [ ] Windows executable (.exe)
- [ ] macOS application (.dmg)
- [ ] First GitHub Release

---

## Version 1.1

- [ ] Playlist support
- [ ] Drag & Drop songs
- [ ] Keyboard shortcuts
- [ ] Themes
- [ ] Recently Played

---

# 💡 Future Ideas

- ☁️ Cloud music library
- 📱 Flutter mobile app
- 🔄 Cross-device sync
- ❤️ Favorites
- 📥 Built-in song downloader
- 🎤 Lyrics support
- 🎚️ Equalizer
- 🎨 Theme store
- 🌙 Dark / Light mode
- 🔍 Instant search
- 📊 Listening statistics

---

# 🤝 Contributing

Contributions, ideas and bug reports are always welcome.

Feel free to open an Issue if you discover a bug or have an idea for a new feature.

---

# 📄 License

MIT License

---

Made with ❤️ using Python.