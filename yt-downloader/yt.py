import yt_dlp

url = input("Enter video url:\n")
download_path = input("Enter the path where you want to save the MP4 file:\n")

ydl_opts = {
    'outtmpl': f"{download_path}/%(title)s.%(ext)s",  # Use outtmpl to specify output template
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully to the specified path!")
