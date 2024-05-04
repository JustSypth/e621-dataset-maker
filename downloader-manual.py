# @title ##Download database off e621 (Optional)
# @markdown ###-I recommend fixing the captioning in the next cell

import requests
import os
import time
from tkinter import filedialog

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

print("                    %                   ")
print("                 %%%%%.                 ")
print("                @@@@@%%                 ")
print("              (@@   @@@                 ")
print("                                        ")
print("        ,,,,,,,,,,,,,,,,,,      .@@%%%% ")
print("      ,,,,,,,,@@@@@@&,,,,,,.  ,@@@@@&%%%")
print("     ,,,,,,@@@@@*,#@@@@*,,,,,     @@%%% ")
print("   ,,,,,,,@@@,,,,,,,,@@@/,,,,,    @@    ")
print("  ,,,,,,,,@@@@@@@@@@@@@@&,,,,,,         ")
print(" ,,,,,,,,,@@@@,,,,,,(,,,,,,,,,,,,       ")
print(" ,,,,,,,,,,,@@@@@@@@@@,,,,,,,,,,        ")
print("   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,         ")
print("    ,,,,,,,,,,,,,,,,,,,,,,,,,           ")
print("      ,,,,,,,,,,,,,,,,,,,,,,            ")
print("       ,,,,,,,,,,,,,,,,,,,,             ")
print()

UserAgent = {"User-Agent": "e621Downloader/1.0 (by JustSypth on e621)"}

print("[E621 MANUAL Dataset Maker]")
print("-Made by JustSypth on GitHub")



try:
    filePathMode = int(input("1. Cli, 2. Window: "))
except:
    input("You have to enter a number")
    exit()

cls()

if filePathMode == 1:
    filepath = input("Paste the directory of your desired location here: ")
if filePathMode == 2:
    filepath = filedialog.askdirectory()


imageorder = 0

while True:

    cls()
    post_id = str(input("Type the id of the post (To cancel press 0): ")) 

    if post_id == "0":
        exit()


    URL = f"https://e621.net/posts/{post_id}.json"
    r = requests.get(url = URL, headers=UserAgent)
    data = r.json()

    time.sleep(1.2)

    imageorder = imageorder + 1

    extension = str(data["post"]["file"]["ext"])
    image_url = str(data["post"]["file"]["url"])

    tags = []
    for category in data["post"]["tags"]:
        tags.extend(data["post"]["tags"][category])


    try:
        # Download the image
        image_data = requests.get(image_url).content
        time.sleep(1)

        with open(f"{filepath}/{imageorder}.{extension}", 'wb') as handler:
            handler.write(image_data)

        # Save the tags to a text file
        with open(f"{filepath}/{imageorder}.txt", "w") as f:
            f.write(", ".join(tags))


    except Exception as e:
        print(f"Failed to download image {post_id}: {e}")
        continue
