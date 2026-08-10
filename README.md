# 🎵 Mashup Web App

A Python-based web application that automatically creates a music mashup from YouTube songs using **Streamlit**.

The user provides a singer/artist name, the number of videos to include, the duration of each clip, and an email address. The application searches YouTube for songs, downloads the videos, extracts their audio, trims each clip, combines them into a single MP3 mashup, compresses the result into a ZIP file, and sends it to the provided email address.

## ✨ Features

* 🎤 Search YouTube songs by singer/artist name
* 🎬 Download multiple YouTube videos automatically
* 🎧 Extract audio from downloaded videos
* ✂️ Trim each song to a specified duration
* 🔀 Merge all clips into one continuous mashup
* 📦 Automatically create a ZIP file
* 📧 Send the generated ZIP file through email
* ⚡ Uses multithreading to speed up downloading and audio processing
* 🌐 Simple and interactive Streamlit interface

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — Web interface
* **YouTube Search Python** — YouTube search
* **PyTube** — YouTube video downloading
* **MoviePy** — Video/audio processing
* **Pydub** — Audio trimming and merging
* **FFmpeg** — Media processing
* **SMTP / Gmail** — Email delivery
* **Concurrent Futures** — Parallel processing

## 📂 Project Structure

```text
mashup-app/
│
├── app.py                 # Streamlit web application
├── mashupcode.py          # Core mashup generation logic
├── SendEmail.py           # Email sending functionality
├── requirements.txt       # Python dependencies
├── packages.txt           # System dependencies
├── setup.sh               # Streamlit configuration
├── procfile               # Deployment configuration
├── .devcontainer/
│   └── devcontainer.json  # Development container configuration
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install FFmpeg

FFmpeg is required for audio/video processing.

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS with Homebrew:**

```bash
brew install ffmpeg
```

**Windows:**

Install FFmpeg and make sure it is available in your system `PATH`.

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Email Configuration

The application uses Streamlit secrets for the sender email credentials.

Create:

```text
.streamlit/secrets.toml
```

and add:

```toml
aq = "your-email@gmail.com"
qib = "your-app-password"
```

### Gmail Setup

For Gmail, use a **Google App Password** rather than your normal Gmail password.

Make sure:

* 2-Step Verification is enabled on the Google account.
* An App Password is generated.
* The App Password is stored in `secrets.toml`.
* `secrets.toml` is **not committed to GitHub**.

Add this to `.gitignore`:

```gitignore
.streamlit/secrets.toml
__pycache__/
*.pyc
audios/
videos/
media/
venv/
```

> ⚠️ Never publish your email password or App Password in a public GitHub repository.

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

By default, Streamlit runs on:

```text
http://localhost:8501
```

## 🖥️ How It Works

The application follows this workflow:

```text
User Input
    │
    ├── Singer Name
    ├── Number of Videos
    ├── Clip Duration
    └── Email Address
           │
           ▼
     Search YouTube
           │
           ▼
   Download Song Videos
           │
           ▼
    Extract Audio Tracks
           │
           ▼
     Trim Audio Clips
           │
           ▼
      Merge All Clips
           │
           ▼
      mashup.mp3
           │
           ▼
       Create ZIP
           │
           ▼
      mashup.zip
           │
           ▼
      Send via Email
```

## 📝 User Inputs

### Singer Name

The artist/singer whose songs should be searched.

Example:

```text
Arijit Singh
```

### Number of Videos

The number of songs/videos to include in the mashup.

The application expects **more than 10 videos**.

Example:

```text
15
```

### Duration

The duration, in seconds, to take from each song.

The application expects a minimum of **20 seconds**.

Example:

```text
30
```

For 15 videos at 30 seconds each, the resulting mashup will contain approximately:

```text
15 × 30 = 450 seconds
```

of audio.

### Email

The email address where the generated ZIP file should be sent.

## 📦 Output

The application generates:

```text
media/
├── mashup.mp3
└── mashup.zip
```

The ZIP file contains the final MP3 mashup.

After the email is successfully sent, temporary folders/files are removed from the application environment.

## ⚡ Performance

The project uses Python's `ThreadPoolExecutor` to perform several operations concurrently, including:

* Downloading videos
* Converting videos to audio
* Extracting audio segments

This helps reduce the overall processing time when handling multiple songs.

## ☁️ Deployment

The project includes configuration for deployment using a platform that supports a `Procfile` and Streamlit.

The included `procfile` contains:

```text
web: sh setup.sh && streamlit run app.py
```

For deployment, make sure the following are configured:

1. Python dependencies are installed.
2. FFmpeg is available.
3. Streamlit secrets are configured.
4. Email credentials are stored securely.
5. The application has sufficient temporary storage for downloaded videos and generated audio.

## 🧑‍💻 Development with GitHub Codespaces

The repository includes a `.devcontainer/devcontainer.json` configuration.

If you open the project in GitHub Codespaces, the development environment can automatically install the required dependencies and start the Streamlit application.

The application uses port:

```text
8501
```

## ⚠️ Important Notes

* YouTube downloading may be affected by changes to YouTube or third-party libraries.
* `pytube` and `youtube-search-python` may require updates if YouTube changes its APIs or web interface.
* Processing a large number of videos can require significant CPU, memory, storage, and network bandwidth.
* Gmail may reject authentication if an App Password or account configuration is incorrect.
* Do not commit credentials, API keys, passwords, or Streamlit secrets to GitHub.

## ⚖️ Copyright & Responsible Use

This project is intended for educational and personal experimentation.

Users are responsible for ensuring that downloaded and processed content is used in accordance with applicable copyright laws, YouTube's Terms of Service, and the rights of content owners.

Only process content that you have permission to download and use.

## 🔮 Future Improvements

Potential improvements include:

* [ ] Add better input validation
* [ ] Add progress indicators
* [ ] Show download/processing status
* [ ] Improve duplicate song detection
* [ ] Add configurable audio fade-in/fade-out
* [ ] Allow users to choose output format
* [ ] Add background task processing
* [ ] Improve YouTube search reliability
* [ ] Add better error handling
* [ ] Support multiple email providers
* [ ] Add automatic cleanup on failed jobs
* [ ] Add a download option directly in the web interface

## 📄 License

This project is available for educational and personal use.

If you plan to publish or distribute this project, consider adding an appropriate open-source license such as the MIT License.

---

⭐ If you found this project useful, consider giving the repository a star!
