# pip install pyshorteners
# pip install pyperclip


import pyshorteners as ps
import pyperclip as  pc

url =input("Enter URL to Shortern: ")

def shortenurl(url):
    s=ps.Shortener()
    print(s.tinyurl.short(url))
    
    
shortenurl(url)    