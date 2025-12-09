import pyshorteners

def short(long_url):
  
    try:
        s = pyshorteners.Shortener()
        short_url = s.isgd.short(long_url)
        return short_url
    except Exception as e:
        return f"error shortening URL: {e}"

if __name__ == "__main__":
    long_url = input("enter the URL to shorten: ")
    short_url = short(long_url)
    print(f"Shortened URL : {short_url}")
