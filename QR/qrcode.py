import segno

def generate_qr_code(website_link):
  """
  Generates a QR code for the provided website link and saves it as an image.

  Args:
    website_link (str): URL of the website for which to generate the QR code.

  Returns:
    None

  Raises:
    ValueError: If the provided website link is invalid.
  """
  # Validate website link
  if not website_link or not website_link.startswith("http"):
    raise ValueError("Invalid website link. Please enter a valid URL.")

  # Create QR code object
  qr_code = segno.make(website_link)

  # Save QR code as image
  image_filename = f"qr_code.png"
  qr_code.save(image_filename)

  print(f"QR code for {website_link} generated and saved as '{image_filename}'.")

# Example usage
if __name__ == "__main__":
  website_link = input("Paste your link:-\n")
  generate_qr_code(website_link)
