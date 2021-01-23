import os

username = os.environ['USERNAME']
CHROME_USER_PROFILES = f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

"""
Windows 7, 8.1, and 10: C:\\Users\\<username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default
Mac OS X El Capitan: Users/<username>/Library/Application Support/Google/Chrome/Default
Linux: /home/<username>/.config/google-chrome/default
"""
