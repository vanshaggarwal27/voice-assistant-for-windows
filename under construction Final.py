from typing import Type                                                                                   #hello  
import speech_recognition as sr                                                                           #show music player
import pyaudio                                                                                            #show pictures(path independent)  
import pyttsx3 as p                                                                                       #empty recycle bin
import os                                                                                                 #join image
from PIL import Image                                                                                     #show desktop
import tkinter as tk                                                                                      #convert images to pdf
from tkinter import filedialog                                                                            #youtube url to audio(nt working )
import pyautogui as py                                                                                    #webp to jpeg
import img2pdf                                                                                            #downlaod video from url        #open youtube
import time                                                                                               #change wallpaper               #open chrome
from pytube import YouTube                                                                                #set timer                      #open gmail
import webbrowser                                                                                         #shutdown pc(avoid)             #open calculator
import ctypes                                                                                             #lock pc                        #open sticky notes
import winshell                                                                                           #restart pc(avoid)              #open vs
import re                                                                                                 #play particular song on youtbe #open calender
import subprocess                                                                                         #close application          
from pathlib import Path                                                                                  #play song on spotify
import platform     
import socket       
import datetime     
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import qrcode
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from tempfile import NamedTemporaryFile


                                                           
f=open("log.txt","a")

def say(txt):
    engine.say(txt)
    engine.runAndWait()
    f.write("Eva:" + txt)
    f.write("\n")
    f.flush()

engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
r = sr.Recognizer()
py.FAILSAFE = False

root = tk.Tk()
root.withdraw()
def is_connected():
    try:
        # Try to connect to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
print("checking for internet connection")

if is_connected():
    
    while True: 

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            
            Text=r.listen(source,timeout=3)
            try:
                recognised_text = r.recognize_google(Text).lower()
                f.writelines("User:" + recognised_text)
                f.write("\n")
                f.flush()
                print(recognised_text)
                engine = p.init() 
                
                if(recognised_text=='hello'):
                    say('hello sir')
                
                if("show logs" in recognised_text):
                    def open_log_file(log_file_name):
                        # Get the current working directory (CWD)
                        cwd = os.getcwd()
                        
                        # Construct the full path to the log file
                        log_file_path = os.path.join(cwd, log_file_name)

                        try:
                            # Open the log file and read its contents
                            with open(log_file_path, 'r') as file:
                                content = file.read()
                                print(f"Contents of {log_file_name}:\n")
                                print(content)
                        except FileNotFoundError:
                            print(f"The file '{log_file_name}' was not found in the current working directory.")
                        except Exception as e:
                            print(f"An error occurred while opening the log file: {e}")

                    # Example usage
                    log_file_name = 'log.txt'
                    open_log_file(log_file_name)
 
                if('show pictures' in recognised_text or "show images" in recognised_text):
                    say('showing images')
                    
                    system_platform = platform.system()
                    if system_platform == "Windows":
                        # On Windows, check for Pictures folder in OneDrive
                        onedrive_pictures_folder = Path(os.path.expanduser("~/OneDrive/Pictures"))
                        if onedrive_pictures_folder.is_dir():
                            print(f"Opening Pictures folder in OneDrive: {onedrive_pictures_folder}")
                            try:
                                subprocess.run(["start", str(onedrive_pictures_folder)], check=True, shell=True)
                            except subprocess.CalledProcessError as e:
                                print(f"Error opening Pictures folder in OneDrive: {e}")
                        else:
                            # If Pictures folder in OneDrive is not found, open the default Pictures folder
                            pictures_folder = Path(os.path.expanduser("~/Pictures"))
                            print(f"Opening default Pictures folder: {pictures_folder}")
                            try:
                                subprocess.run(["start", str(pictures_folder)], check=True, shell=True)
                            except subprocess.CalledProcessError as e:
                                print(f"Error opening default Pictures folder: {e}")
                
                if ("open youtube" in recognised_text or "open YouTube" in recognised_text):
                    say("opening youtube")
                    webbrowser.open("youtube.com")
                     
                
                if("open camera" in recognised_text):
                    say("opening camera")
                    
                    subprocess.run(["start", "microsoft.windows.camera:"], shell=True)

                if("open whatsapp" in recognised_text):
                    say("opening whatsapp ")
                    
                    subprocess.run(["start", "whatsapp:"], shell=True)
                
                if("open sticky note" in recognised_text or "open sticky notes" in recognised_text ):
                    say("opening sticky notes")
                    
                    subprocess.run(["start", "shell:AppsFolder\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App"], shell=True, creationflags=subprocess.CREATE_NO_WINDOW) 
                
                if("open vs" in recognised_text or "open vs code" in recognised_text or "open visual studio" in recognised_text):
                    say("opening visual studio ")
                    
                    subprocess.run(["start", "vscode:"], shell=True)
                if("open calculator" in recognised_text):
                    say('opening calculator')
                    
                    subprocess.run("calc.exe")
                if ("open insta" in recognised_text or "open instagram" in recognised_text):
                    say("opening Iinstagram")
                    
                    webbrowser.open("https://www.instagram.com/", new=2)       
                if ('play music' in recognised_text):
                    say('starting music player')
                    
                    os.startfile(r"D:\programs\music_player.exe")
                
                if('open chrome' in recognised_text):
                    say('starting google chrome')
                    
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                
                if("show mails" in recognised_text or "show mail" in recognised_text or "open gmail" in recognised_text or "show males" in recognised_text): 
                    say("opening gmail")
                    
                    webbrowser.open("mail.google.com/mail/u/0/#inbox")
                    
                if("change wallpaper" in recognised_text or "change background" in recognised_text):
                    def set_wallpaper(path):
                        SPI_SETDESKWALLPAPER = 20
                        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

                    file_path = filedialog.askopenfilename(title="Select Wallpaper", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
                    if (file_path):
                        set_wallpaper(file_path)
                    say("wallpaper changed")
                      

                if("shutdown pc" in recognised_text or "shut down my pc" in recognised_text or "shutdown my pc" in recognised_text):
                    say("are you sure to shutdown pc?")
                    
                    with sr.Microphone() as source:
                        shut_pc=r.listen(source)
                        try:
                            rec_shut = r.recognize_google(shut_pc)
                            if(rec_shut=="yes"or "yeah"):
                                os.system("shutdown /s /t 1")
                            else:
                                say("ok.. you can continue to work")
                                
                        except sr.UnknownValueError:
                            say('i cant recognise that')
                             

                if("lock pc" in recognised_text or "lock my pc" in recognised_text):
                    say("locking your pc")
                    
                    ctypes.windll.User32.LockWorkStation()

                if("restart" in recognised_text or "restart my pc" in recognised_text):
                    say("are you sure to restart")
                    
                    with sr.Microphone() as source:
                        restart_pc=r.listen(source)
                        try:
                            rec_rest = r.recognize_google(restart_pc)
                            if(rec_rest=="yes"or "yeah"):
                                os.system("shutdown /r /t 0")
                            else:
                                say("ok.. you can continue to work")
                                
                        
                        except sr.UnknownValueError:
                            say('i cant recognise that')
                             
            
            
                if('url to audio' in recognised_text or 'URL to audio' in recognised_text or "download song from youtube" in recognised_text):
                    say('type url of video')
                    
                    x= os.getcwd()
                    # url input from user
                    a=py.prompt('enter url of video you want to convert to audio')
                    yt = YouTube(str(a))
                    time.sleep(1)
                    say("downloading audio.. please wait")
                    
                    # extract only audio
                    video = yt.streams.filter(only_audio=True).first()

                    # check for destination to save file
                    say("Enter the destination")
                    
                    b=py.prompt("Enter the destination (leave blank for current directory)")
                    destination = str(b) or '.'

                    # download the file
                    out_file = video.download(output_path=destination)

                    # save the file
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)

                    # result of success
                    py.alert(yt.title + " has been successfully downloaded.")
                    os.startfile(x)      

                if('image to pdf' in recognised_text or 'images to pdf' in recognised_text):
                    say('select images')
                    
                    
                    def convert_images_to_pdf(image_paths, output_path):
                        with open(output_path, "wb") as f:
                            f.write(img2pdf.convert(image_paths))

                    # create tkinter window to select files
                    root = tk.Tk()
                    root.withdraw()
                    file_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
                    if not file_paths:
                        print("No files selected.")
                        exit()
                    say('select location to save pdf')
                    
                    # get directory of first file selected to use for output file path
                    output_dir = os.path.dirname(file_paths[0])

                    # create tkinter window to select output file name and location
                    root = tk.Tk()
                    root.withdraw()
                    output_path = filedialog.asksaveasfilename(title="Save PDF File", defaultextension=".pdf", initialdir=output_dir)

                    # convert images to pdf
                    convert_images_to_pdf(file_paths, output_path)
                    say("PDF file created!! ")
                    

                if('join image'  in recognised_text):
                    say('select the images')
                    
                    
                    im1_path = filedialog.askopenfilename()
                    im2_path = filedialog.askopenfilename()

                    # main()
                    im1 = Image.open(im1_path)
                    im2 = Image.open(im2_path)

                    def get_concat_h_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
                        if im1.height == im2.height:
                            _im1 = im1
                            _im2 = im2
                        elif (((im1.height > im2.height) and resize_big_image) or
                            ((im1.height < im2.height) and not resize_big_image)):
                            _im1 = im1.resize((int(im1.width * im2.height / im1.height), im2.height), resample=resample)
                            _im2 = im2
                        else:
                            _im1 = im1
                            _im2 = im2.resize((int(im2.width * im1.height / im2.height), im1.height), resample=resample)
                        dst = Image.new('RGB', (_im1.width + _im2.width, _im1.height))
                        dst.paste(_im1, (0, 0))
                        dst.paste(_im2, (_im1.width, 0))
                        return dst

                    def get_concat_v_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
                        if im1.width == im2.width:
                            _im1 = im1
                            _im2 = im2
                        elif (((im1.width > im2.width) and resize_big_image) or
                            ((im1.width < im2.width) and not resize_big_image)):
                            _im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), resample=resample)
                            _im2 = im2
                        else:
                            _im1 = im1
                            _im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), resample=resample)
                        dst = Image.new('RGB', (_im1.width, _im1.height + _im2.height))
                        dst.paste(_im1, (0, 0))
                        dst.paste(_im2, (0, _im1.height))
                        return dst

                    say('join images vertically or horizontally?')
                    
                    
                    with sr.Microphone() as source:
                        Type_image=r.listen(source)
                        try:
                            recognised_text = r.recognize_google(Type_image)
                            
                            if(recognised_text == "vertically" or"vertical" ):
                                get_concat_v_resize(im1, im2, resize_big_image=False).save(r"C:\Users\HP\OneDrive\Pictures\Saved Pictures\Merged image.jpg")        
                                os.startfile(r'C:\Users\HP\OneDrive\Pictures\Saved Pictures\Merged image.jpg')
                                say('succesfully merged')
                                
                                print(recognised_text)
                            
                            elif(recognised_text == "horizontally" or "horizontal" ):
                                get_concat_h_resize(im1, im2).save(r"C:\Users\HP\OneDrive\Pictures\Saved Pictures\Merged image.jpg")
                                os.startfile(r'C:\Users\HP\OneDrive\Pictures\Saved Pictures\Merged image.jpg')
                                say('succesfully merged')
                                
                                print(recognised_text)
                        
                        except sr.UnknownValueError:
                            print('cant recognize that')
                        except sr.RequestError as e:
                            print('sorry')

                if("empty recycle bin" in recognised_text or "clear recycle bin" in recognised_text):
                    say("Plase wait..empting recycle bin")
                    
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    say("Recyle bin cleared")
                    

                if('wep to jpg' in recognised_text or "wep to jpeg"  in recognised_text or "web to jpeg"  in recognised_text or "web to jpg"  in recognised_text):
                    say('select the file')
                    
                    def convert_image():
                        # open file dialog to select the image file
                        file_path = filedialog.askopenfilename(filetypes=[("WebP Files", "*.webp")])
                        
                        if file_path:
                            # open the image and convert it to jpeg
                            with Image.open(file_path) as img:
                                img = img.convert("RGB")
                                jpeg_path = file_path[:-5] + ".jpeg"
                                img.save(jpeg_path, "jpeg")
                                tk.messagebox.showinfo("Success", f"Image converted and saved as {jpeg_path}")
                                os.startfile(jpeg_path)
                        else:
                            tk.messagebox.showwarning("Warning", "Please select a valid WebP image file")

                    # create the main window and add widgets
                    root = tk.Tk()
                    root.title("WebP to JPEG Converter")
                    root.geometry("400x150")

                    # add title label
                    title_label = tk.Label(root, text="Convert WebP to JPEG", font=("Calibri", 15))
                    title_label.pack(pady=10)

                    # add convert button
                    convert_btn = tk.Button(root, text="Convert", font=("Calibri", 14), command=convert_image)
                    convert_btn.pack(pady=10)

                    # start the main event loop
                    root.mainloop()
                
                if("play" in recognised_text and "on youtube" in recognised_text):
                    a=recognised_text.replace("play", "playing")
                    say(a)
                    
                    def extract_song_name(command):
                    # Use regular expression to extract the song name
                
                        match = re.search(r'play\s+(.*?)\s+on\s+youtube', command, re.IGNORECASE)
                        if match:
                            return match.group(1)
                        else:
                            return None

                    def play_on_youtube(song_name):
                    # Construct the YouTube search URL
                        search_url = f"https://www.youtube.com/results?search_query={song_name}"
                    # Open the web browser to the YouTube search URL
                        webbrowser.open(search_url)
                    # Get user input
                    user_input = recognised_text
                    # Extract the song name
                    song_name = extract_song_name(user_input)

                    play_on_youtube(song_name)
                    time.sleep(9)
                    py.moveTo(637,486)
                    py.click()
                
                if('show desktop' in recognised_text or 'show text top' in recognised_text): 
                    say('showing desktop')
                    
                    x=py.position()
                    y=py.size()
                    py.moveTo(y)
                    py.doubleClick()
                    py.moveTo(x)      
                
                if ("show calender" in recognised_text or "open calender" in recognised_text):
                    say('showing calender')
                    
                    x1=py.position()
                    py.moveTo(x=1845, y=1052)
                    py.click()
                    py.moveTo(x1)

                if ("url to video" in recognised_text or "url 2 video" in recognised_text or "url 2 Video" in recognised_text or "url to video" in recognised_text or "video from url" in recognised_text or "video from youtube" in recognised_text):
                    def download_video(url):
                        try:
                            yt = YouTube(url)
                            video = yt.streams.get_highest_resolution()
                            video.download(output_path=r"D:\videos")
                            print("Video downloaded successfully!")
                        except Exception as e:
                            print("Error downloading video:", str(e))

                    url = py.prompt("Enter the YouTube video URL: ")
                    # Download video
                    download_video(url)
                if ('set timer for' in recognised_text):
                    def convert_to_seconds(duration, unit):
                        if unit.lower() == 'seconds':
                            return duration
                        elif unit.lower() == 'minutes' or unit.lower() == 'minute' :
                            return duration * 60
                        elif unit.lower() == 'hours':
                            return duration * 3600
                        else:
                            raise ValueError("Invalid time unit. Please enter 'seconds', 'minutes', or 'hours'.")

                    def set_timer(duration, unit):
                        seconds = convert_to_seconds(duration, unit)
                        print(f"Timer set for {duration} {unit}. Press Ctrl+C to stop.")
                        say(f"Timer set for {duration} {unit}.")
                        
                        try:
                            time.sleep(seconds)
                            print("Time's up!")
                            say("Time's up!")
                            
                        except KeyboardInterrupt:
                            print("Timer stopped manually.")
                            say("Timer stopped manually.")
                            
                                
                    duration_str = recognised_text.replace("set timer for", "").strip()
                    duration,unit = duration_str.split()
                    duration = int(duration)
                    set_timer(duration, unit)
                if ("time" in recognised_text):
                    current_time = datetime.datetime.now().strftime("%I %M %p")
                    engine.say("The current time is " + current_time)

                if ("jpeg to png" in recognised_text or "jpg to png" in recognised_text):
                    def jpeg_to_png(input_path, output_path):
                        try:
                            img = Image.open(input_path)
                            if img.format == 'JPEG':
                                img.save(output_path, 'PNG')
                                print(f"Converted {input_path} to {output_path}")
                            else:
                                print(f"Input file {input_path} is not a JPEG image.")
                        except IOError:
                            print(f"Unable to open or convert {input_path}")

                    def select_file():
                        root = tk.Tk()
                        root.withdraw()  # Hide the main window

                        # Prompt user to select a file
                        file_path = filedialog.askopenfilename()
                        return file_path

                    def main():
                        file_path = select_file()
                        if not file_path:
                            print("No file selected. Exiting.")
                            return

                        # Define output file name
                        output_path = file_path.rsplit('.', 1)[0] + '.png'

                        # Convert JPEG to PNG
                        jpeg_to_png(file_path, output_path)

                    if __name__ == "__main__":
                        main()
                    say("conversion succesfull")
                
                if ("png to jpeg" in recognised_text or "png to jpg" in recognised_text):
                    def png_to_jpeg(input_path, output_path):
                        try:
                            img = Image.open(input_path)
                            if img.format == 'PNG':
                                img.save(output_path, 'JPEG')
                                print(f"Converted {input_path} to {output_path}")
                            else:
                                print(f"Input file {input_path} is not a PNG image.")
                        except IOError:
                            print(f"Unable to open or convert {input_path}")

                    def select_file():
                        root = tk.Tk()
                        root.withdraw()  # Hide the main window

                        # Prompt user to select a file
                        file_path = filedialog.askopenfilename()
                        return file_path

                    def main():
                        file_path = select_file()
                        if not file_path:
                            print("No file selected. Exiting.")
                            return

                        # Define output file name
                        output_path = file_path.rsplit('.', 1)[0] + '.jpg'

                        # Convert PNG to JPEG
                        png_to_jpeg(file_path, output_path)

                    if __name__ == "__main__":
                        main()
                    say("conversion succesfull")

                if ("close" in recognised_text):  #close application
                    
                    def extract_application_name(command):
                        # Define a pattern to match common application-related words
                        # This pattern assumes the application name is a word or a phrase following keywords like 'close', 'kill', or 'exit'
                        pattern = r'\b(?:close|kill|exit)\s+(.*)'

                        # Use re.search to find the pattern in the command
                        match = re.search(pattern, command, re.IGNORECASE)
                        
                        if match:
                            app_name = match.group(1).strip()
                            return app_name if app_name else "No application name found."
                        else:
                            return "No application name found."

                    command = recognised_text
                    app = extract_application_name(command)
                    say("closing"+ app)

                    def close_application_windows():
                        app_name = app

                        try:
                            # Attempt to close a traditional .exe application
                            response = os.system(f'taskkill /f /im {app_name}.exe')
                            if response == 128:  # 128 indicates that the process name was not found
                                print("")
                                # Use PowerShell to try to close a UWP app
                                close_uwp_app(app_name)
                            elif response == 0:
                                print()
                        except Exception as e:
                            print(f"An error occurred: {e}")

                    def close_uwp_app(app_name):
                        try:
                            # Hide the console window by setting the creation flags
                            startupinfo = subprocess.STARTUPINFO()
                            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                            # Use PowerShell to close a UWP app without popping up a shell window
                            subprocess.run(
                                ["powershell", "-Command", f"Get-Process | Where-Object {{$_.MainWindowTitle -like '*{app_name}*'}} | Stop-Process"],
                                startupinfo=startupinfo,
                                check=True
                            )
                            print(f"")
                        except subprocess.CalledProcessError:
                            print(f"")

                    # Run the function
                    close_application_windows()
                if ("play" in recognised_text and "on spotify" in recognised_text):
                    say("playing on Spottify")
                    def extract_song_name(command):
                        # Define the regex pattern to match the format 'play <song_name> on spotify'
                        pattern = r"play (.+?) on spotify"
                        
                        # Search for the pattern in the input command
                        match = re.search(pattern, command, re.IGNORECASE)
                        
                        if match:
                            # Extract the song name from the matched pattern
                            song_name= match.group(1).strip()
                            return song_name
                        else:
                            return None

                    if __name__ == "__main__":
                        # Prompt the user for input
                        command = recognised_text
                        # Extract the song name from the user input
                        song_name1 = extract_song_name(command)
                    # Replace these with your Spotify app credentials
                    CLIENT_ID = 'your api keys'
                    CLIENT_SECRET = 'your api keys'
                    REDIRECT_URI = 'http://localhost:8888/callback'  # Make sure this URI is added in your Spotify app settings

                    # Scope for searching tracks
                    SCOPE = 'user-read-private'

                    # Authenticate with Spotify
                    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                                client_secret=CLIENT_SECRET,
                                                                redirect_uri=REDIRECT_URI,
                                                                scope=SCOPE))

                    def open_song_in_spotify(song_name):
                        # Convert song name to lowercase to handle case insensitivity
                        song_name_lower = song_name.lower()
                        
                        # Search for the song on Spotify
                        results = sp.search(q=song_name_lower, type='track', limit=1)
                        
                        if results['tracks']['items']:
                            track = results['tracks']['items'][0]
                            track_name = track['name'].lower()  # Convert track name to lowercase for comparison

                            # Check if the search result matches the input (ignoring case)
                            if song_name_lower in track_name:
                                track_url = track['external_urls']['spotify']
                                
                                # Open the track in the Spotify app or web player
                                webbrowser.open(track_url)
                                print(f"Opening {track['name']} by {track['artists'][0]['name']} in Spotify...")
                            else:
                                print(f"Exact match for '{song_name}' not found. Showing closest match.")
                                track_url = track['external_urls']['spotify']
                                webbrowser.open(track_url)
                        else:
                            print(f"Song '{song_name}' not found on Spotify.")

                    if __name__ == "__main__":
                        song_name = song_name1
                        open_song_in_spotify(song_name)

                if("make qr" in recognised_text or "generate qr" in recognised_text or "make qr code" in recognised_text or "generate qr code" in recognised_text):
                    say("okay")
                    def generate_qr_code(url, temp_file_path):
                        try:
                            # Generate QR code instance
                            qr = qrcode.QRCode(
                                version=1,
                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                box_size=10,
                                border=4,
                            )

                            # Add data to the QR code
                            qr.add_data(url)
                            qr.make(fit=True)

                            # Generate an image from the QR code
                            img = qr.make_image(fill_color="black", back_color="white")
                            img.save(temp_file_path)
                            print(f"QR code saved to temporary file: {temp_file_path}")

                            return True
                        except Exception as e:
                            print(f"Error generating QR code: {e}")
                            return False

                    class QRCodeGeneratorApp(QWidget):
                        def __init__(self):
                            super().__init__()
                            self.initUI()

                        def initUI(self):
                            self.setWindowTitle('QR Code Generator')
                            self.setGeometry(100, 100, 400, 500)

                            # Set main layout
                            main_layout = QVBoxLayout()
                            main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

                            # Title label
                            title_label = QLabel("QR Code Generator")
                            title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                            title_label.setFont(QFont('Arial', 16, QFont.Weight.Bold))
                            title_label.setStyleSheet("color: black;")
                            main_layout.addWidget(title_label)

                            # URL input
                            self.url_input = QLineEdit(self)
                            self.url_input.setPlaceholderText('Enter the URL')
                            self.url_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
                            self.url_input.setStyleSheet("font-size: 14px; padding: 8px; color: black; background-color: white;")
                            main_layout.addWidget(self.url_input)

                            # Generate button
                            self.generate_button = QPushButton('Generate QR Code', self)
                            self.generate_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 8px; border-radius: 4px;")
                            self.generate_button.clicked.connect(self.on_generate_button_click)
                            main_layout.addWidget(self.generate_button)

                            # Spacer for better layout
                            main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

                            # QR code display container
                            qr_container_layout = QHBoxLayout()
                            qr_container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                            
                            # QR code display
                            self.qr_label = QLabel(self)
                            self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                            self.qr_label.setFixedSize(300, 300)
                            qr_container_layout.addWidget(self.qr_label)

                            main_layout.addLayout(qr_container_layout)

                            # Add a bottom spacer to push QR code to the center
                            main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

                            # Set the layout and background color
                            self.setLayout(main_layout)
                            self.setStyleSheet("background-color: #f0f0f0;")

                            # Create a temporary file to save the QR code image
                            self.temp_file = NamedTemporaryFile(suffix='.png', delete=False)
                            self.temp_file.close()

                        def on_generate_button_click(self):
                            url = self.url_input.text()
                            if url:
                                success = generate_qr_code(url, self.temp_file.name)
                                if success:
                                    try:
                                        # Load the image from the file and display it
                                        pixmap = QPixmap(self.temp_file.name)
                                        scaled_pixmap = pixmap.scaled(self.qr_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
                                        self.qr_label.setPixmap(scaled_pixmap)
                                    except Exception as e:
                                        print(f"Error displaying QR code: {e}")
                                        QMessageBox.critical(self, "Error", f"Failed to display QR code: {e}")
                                else:
                                    QMessageBox.warning(self, "Error", "Could not generate QR code. Please check the URL.")
                            else:
                                QMessageBox.warning(self, "Input Error", "Please enter a valid URL.")

                        def closeEvent(self, event):
                            # Cleanup: Remove the temporary file on close
                            os.remove(self.temp_file.name)
                            event.accept()

                    def main():
                        app = QApplication(sys.argv)
                        window = QRCodeGeneratorApp()
                        window.show()
                        sys.exit(app.exec())

                    if __name__ == "__main__":
                        main()

                if ("stop" in recognised_text):
                    say('ok sir')
                    break

            except sr.UnknownValueError:
                say('')
                
            except sr.RequestError as e:
                print('')
else:
    say("please connect to internet")
    
