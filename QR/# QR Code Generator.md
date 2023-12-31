 # QR Code Generator

This Python script generates a QR code for a given website link and saves it as an image. It uses the `segno` library to create the QR code and save it as a PNG image.

## Step-by-Step Explanation

### 1. Importing the `segno` Library

```python
import segno
```

The first step is to import the `segno` library, which is used to generate QR codes.

### 2. Defining the `generate_qr_code` Function

```python
def generate_qr_code(website_link):
```

The `generate_qr_code` function takes a single argument, `website_link`, which is the URL of the website for which to generate the QR code.

### 3. Validating the Website Link

```python
  # Validate website link
  if not website_link or not website_link.startswith("http"):
    raise ValueError("Invalid website link. Please enter a valid URL.")
```

Before generating the QR code, the function validates the website link to ensure that it is a valid URL. If the link is empty or does not start with "http", the function raises a `ValueError` exception.

### 4. Creating the QR Code Object

```python
  # Create QR code object
  qr_code = segno.make(website_link)
```

Once the website link is validated, the function creates a QR code object using the `segno.make()` function. This function takes the website link as an argument and returns a QR code object.

### 5. Saving the QR Code as an Image

```python
  # Save QR code as image
  image_filename = f"qr_code.png"
  qr_code.save(image_filename)
```

The QR code object is then saved as a PNG image using the `save()` method. The image is saved with the filename "qr_code.png".

### 6. Printing a Success Message

```python
  print(f"QR code for {website_link} generated and saved as '{image_filename}'.")
```

Finally, the function prints a success message indicating that the QR code has been generated and saved.

### 7. Example Usage

```python
# Example usage
if __name__ == "__main__":
  website_link = input("Paste your link:-\n")

