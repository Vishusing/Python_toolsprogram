 # Text-to-Speech Reader

This Python script uses the PyPDF2 and pyttsx3 libraries to read and speak text from a file. It supports both text files (.txt) and PDF files (.pdf).

## Step-by-Step Explanation

### 1. Importing Libraries

```python
import PyPDF2
import pyttsx3
import os
```

We import the necessary libraries:

- `PyPDF2`: This library is used to read and extract text from PDF files.
- `pyttsx3`: This library is used to convert text to speech.
- `os`: This library is used to check if a file exists.

### 2. Initializing pyttsx3 Engine

```python
engine = pyttsx3.init()
```

We initialize the pyttsx3 engine. This engine is responsible for converting text to speech.

### 3. Defining the `read_and_speak` Function

```python
def read_and_speak(file_path):
```

We define a function called `read_and_speak` that takes a `file_path` as an argument. This function is responsible for reading the text from the file and speaking it out loud.

### 4. Checking File Type and Extension

```python
if file_path.endswith(".txt"):
  with open(file_path, "r") as f:
    text = f.read()
elif file_path.endswith(".pdf"):
  # Read PDF content
  reader = PyPDF2.PdfFileReader(open(file_path, "rb"))
  text = ""
  for page in reader.pages:
    text += page.extractText()
else:
  print(f"File format not supported: {file_path}")
  return
```

We check the file type and extension of the given file path. If it's a text file (.txt), we simply read the text from the file. If it's a PDF file (.pdf), we use the PyPDF2 library to extract the text from each page and concatenate it into a single string. If the file format is not supported, we print an error message and return.

### 5. Speaking the Text

```python
engine.say(text)
engine.runAndWait()
```

We use the pyttsx3 engine to speak the extracted text.
