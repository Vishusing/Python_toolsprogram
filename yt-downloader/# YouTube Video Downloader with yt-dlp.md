 # YouTube Video Downloader with yt-dlp

This Python script uses the `yt-dlp` library to download YouTube videos in MP4 format. It prompts the user for the video URL and the desired download path, then uses `yt-dlp` to download the video and save it to the specified location.

## Step-by-Step Explanation

### 1. Importing the `yt_dlp` Library

```python
import yt_dlp
```

This line imports the `yt-dlp` library, which is a command-line tool for downloading videos from YouTube and other video-sharing websites. It provides a Python API that can be used to download videos programmatically.

### 2. Prompting the User for Input

```python
url = input("Enter video url:\n")
download_path = input("Enter the path where you want to save the MP4 file:\n")
```

These lines prompt the user to enter the URL of the video they want to download and the path where they want to save the downloaded MP4 file. The user's input is stored in the `url` and `download_path` variables, respectively.

### 3. Setting up the `yt-dlp` Options

```python
ydl_opts = {
    'outtmpl': f"{download_path}/%(title)s.%(ext)s",  # Use outtmpl to specify output template
}
```

These lines set up the options for the `yt-dlp` downloader. The `outtmpl` option specifies the output template for the downloaded file. In this case, it uses the `%(title)s` and `%(ext)s` placeholders to generate a filename based on the video's title and extension.

### 4. Downloading the Video

```python
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

These lines create a `YoutubeDL` object with the specified options and use it to download the video at the specified URL. The `download()` method takes a list of URLs as input and downloads each video to the specified output path.

### 5. Printing a Success Message

```python
print("Video downloaded successfully to the specified path!")
```

This line prints a success message to the console once the video has been downloaded successfully.

## Conclusion
