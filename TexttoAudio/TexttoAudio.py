import PyPDF2
import pyttsx3
import os

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Function to read and speak text from a file
def read_and_speak(file_path):
  # Check file type and extension
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

  # Speak the text
  engine.say(text)
  engine.runAndWait()

# User input for file path
file_path = input("Enter file path: ")

# Check if file exists
if not os.path.exists(file_path):
  print(f"File not found: {file_path}")
  exit()

# Read and speak the file
read_and_speak(file_path)

print("Done!")

# Release engine resources
engine.stop()
