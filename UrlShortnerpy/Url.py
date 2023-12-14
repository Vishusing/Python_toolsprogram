import pyshorteners

s = pyshorteners.Shortener(api_key='11cbdb02354b211b003285235159571fce674e0b')

def shorten_url(url):
  short_url = s.bitly.short(url)
  return short_url

# Example usage
print('----------------------------------------')
print('URL SHORTNER')
print('-----------------------------------------')
url = input('Enter a your long and bulky url:-\n')
short_url = shorten_url(url)

if short_url:
  print(f"Original URL: {url}")
  print(f"Shortened URL: {short_url}")
else:
  print("Failed to shorten the URL.")
