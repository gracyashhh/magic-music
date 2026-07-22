# 🎵 Magic Music

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS-success)
![License](https://img.shields.io/badge/License-MIT-green)

A fast, lightweight, offline desktop music player built with **Python** and **Eel**.

Magic Music started as a personal project to learn Python and desktop application development. It has gradually evolved into a cross-platform offline music player focused on simplicity, speed and an ad-free experience.

> **Mission:** Create a beautiful, completely free desktop music player that anyone can use without ads or subscriptions.

Designed to run on both **Windows** and **macOS** using the same codebase.

---

# ✨ Features

- 🎵 Play local MP3 files
- 🖼️ Automatically fetch album artwork from Spotify
- ⏯️ Play / Pause
- ⏭️ Next / Previous
- 🔀 Shuffle mode
- 🔁 Repeat mode
- 🔊 Volume control
- ⏱️ Progress bar & seeking
- 📂 Automatically loads songs from the music folder
- 💻 Desktop interface built using HTML, CSS, JavaScript and Python

---

# 🎬 Demo

**Coming soon**

*A short demo GIF will be added after the first stable release.*

---

# 📷 Screenshots

**Coming soon**

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
magic-music/
│
├── getting-started-with-eel/
│   ├── music-player.py
│   ├── cover_art.py
│   ├── web/
│   └── MagicMusicSongs/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> **Note:** The project folder will be renamed in a future cleanup update.

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
python app/music-player.py
```

---

# 🎵 Adding Music

Copy your MP3 files into

```text
getting-started-with-eel/
└── MagicMusicSongs/
```

The application automatically scans and loads all supported audio files inside this folder.

---

# ⚠️ Known Issues

- Empty music folder currently causes an error (planned fix).
- Album artwork depends on Spotify search results.
- Some uncommon audio formats may require conversion before playback.

---

# 📝 Development

Magic Music is actively being developed.

Feature requests, improvements and bug reports are tracked using **GitHub Issues**.

Current development focuses on:

- 🎵 Improving the desktop player
- 🖥️ Windows (.exe) packaging
- 🍎 macOS (.dmg) packaging
- ☁️ Cloud music support
- 📱 Flutter mobile companion app

If you discover a bug or have an idea, feel free to open an Issue.

---

# 🗺️ Roadmap

## 🎯 Version 1.0

- [ ] Handle empty music folder gracefully
- [ ] Better error messages
- [ ] Improve loading performance
- [ ] Better Spotify search matching
- [ ] Windows executable (.exe)
- [ ] macOS application (.dmg)
- [ ] First GitHub Release

## 🚀 Version 1.1

- [ ] Playlist support
- [ ] Drag & Drop songs
- [ ] Keyboard shortcuts
- [ ] Theme support
- [ ] Recently Played

---

# 💡 Future Ideas

- ☁️ Cloud music library
- 📥 Built-in song downloader
- ❤️ Favorites
- 🎤 Lyrics support
- 🎚️ Equalizer
- 🌙 Dark / Light mode
- 🔍 Instant search
- 📊 Listening statistics
- 📱 Flutter mobile application
- 🔄 Cross-device sync

---

# 🤝 Contributing

Contributions, ideas and bug reports are welcome.

Feel free to open an Issue or submit a Pull Request.

---

# 📄 License

MIT License.

---

Made with ❤️ using Python.