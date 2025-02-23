# 🗣️ Voice Assistant

## 🚀 Overview
A Python-based **AI Voice Assistant** that listens to commands and performs various tasks, such as **opening applications, playing music, converting files, managing system settings, and more**.

## ✨ Features
✔ **Voice Commands** – Hands-free interaction using speech recognition.  
✔ **Application Control** – Open/close apps like Chrome, VS Code, WhatsApp.  
✔ **Media Handling** – Convert images, merge images, generate QR codes.  
✔ **Internet & Entertainment** – Play music on **YouTube & Spotify**, open websites.  
✔ **System Operations** – Lock, restart, shutdown, change wallpaper, show desktop.  
✔ **File Management** – Convert images to **PDF**, clean recycle bin.  
✔ **YouTube Downloader** – Download videos/audio from YouTube.  

## 🛠️ Installation
Ensure you have **Python 3.x** installed. Then, install dependencies:  
```sh
pip install speechrecognition pyaudio pyttsx3 pillow tkinter pyautogui img2pdf pytube webbrowser winshell spotipy qrcode PyQt6
```

## 🎙️ How to Use  
Run the script and speak commands like:  

- **"Open YouTube"**  
- **"Play music on Spotify"**  
- **"Convert images to PDF"**  
- **"Lock my PC"**  
- **"Generate QR code"**  

## ⚠️ Known Issues  
- Some system-related commands may require **administrator privileges**.  
- Spotify playback requires **API credentials** in `CLIENT_ID` and `CLIENT_SECRET`.  

## 📜 License  
This project is licensed under the **MIT License**.  

