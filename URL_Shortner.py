import pyshorteners
import pyperclip

url= input('Enter the URL')

def shortenurl(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)