 # URL Shortener

This Python script uses the `pyshorteners` library to shorten long URLs using the Bitly API. It provides a user-friendly interface to easily shorten URLs and display the results.

## Prerequisites

To use this script, you will need to:

1. Install Python 3 or later.
2. Install the `pyshorteners` library using `pip install pyshorteners`.
3. Obtain a Bitly API key from the Bitly website.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the `url_shortener.py` script is located.
2. Run the script using the following command:

```
python url_shortener.py
```

3. You will be prompted to enter a long URL. Enter the URL and press Enter.
4. The script will shorten the URL using the Bitly API and display the original and shortened URLs.

## Code Explanation

The following is a step-by-step explanation of the code:

1. Import the `pyshorteners` library:

```python
import pyshorteners
```

2. Create a `Shortener` object using your Bitly API key:

```python
s = pyshorteners.Shortener(api_key='YOUR_API_KEY')
```

3. Define a function called `shorten_url` that takes a URL as input and returns the shortened URL:

```python
def shorten_url(url):
  short_url = s.bitly.short(url)
  return short_url
```

4. In the `main` function, prompt the user to enter a long URL:

```python
url = input('Enter a your long and bulky url:-\n')
```

5. Call the `shorten_url` function to shorten the URL:

```python
short_url = shorten_url(url)
```

6. Check if the `short_url` is not empty (i.e., the URL was successfully shortened):

```python
if short_url:
```

7. If the URL was successfully shortened, display the original and shortened URLs:

```python
  print(f"Original URL: {url}")
  print(f"Shortened URL: {short_url}")
```

8. If the URL was not successfully shortened, display an error message:
