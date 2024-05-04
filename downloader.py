# @title ##Download database off e621 (Optional)
# @markdown ###-I recommend fixing the captioning in the next cell

import requests
import os
import time
from tkinter import filedialog

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def checkValidTags(data):
    if len(data["posts"]) == 0:
        cls()
        input("You entered invalid tags...")
        exit()

def postCount(tags, limit):
    amount = 0
    i = 0

    if limit == 320:
        while True:
            cls()
            print("Calculating amount of posts.. (The calculating time depends on the amount of posts)")

            time.sleep(1.2)
            i += 1
            URL = f"https://e621.net/posts.json?page={i}&limit={limit}&tags={tags}"
            rTags = requests.get(url = URL, headers=UserAgent)
            time.sleep(1)
            postData = rTags.json()
            checkValidTags(postData)

            if len(postData["posts"]) == 320:
                amount += 320
                isDone = False
            else:
                amount += len(postData["posts"])
                isDone = True

            if isDone == True:
                time.sleep(5)
                break
        return amount

    else:
        return limit
        
        
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

print("[E621 Dataset Maker]")
print("-Made by JustSypth on GitHub")

tags = input("What are the tags: ")
tags = tags.replace(" ", "+")
limit = int(input("How many posts do you want to save (0 for unlimited): "))
if limit == 0:
    limit = 320

postAmount = postCount(tags, limit)
print(f"Total amount of posts ready to download: {postAmount}")

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

i = -1
imageOrder = 0

postID_Url = f"https://e621.net/posts.json?limit=1&tags={tags}"
postID_Request = requests.get(url = postID_Url, headers=UserAgent)
time.sleep(1)
postID_Data = postID_Request.json()
currentID = postID_Data["posts"][0]["id"]

while imageOrder < postAmount:
    i += 1
    URL = f"https://e621.net/posts.json?page=b{currentID}&limit={limit}&tags={tags}"
    r = requests.get(url = URL, headers=UserAgent)
    data = r.json()

    time.sleep(1)

    length = len(data["posts"]) - 1
    currentID = data["posts"][length]["id"]

    fileList = []
    tagList = []

    for x in range(0, len(data["posts"])):
        if data["posts"][x]["file"]["url"] != "None":
            fileList.append(data["posts"][x]["file"]["url"])
            all_tags = []
            for category in data["posts"][x]["tags"]:
                all_tags.extend(data["posts"][x]["tags"][category])
            tagList.append(all_tags)

    for y in range(0, len(fileList)):
        cls()
        print(f"Downloading File {imageOrder} of {postAmount}")

        percentage = round(imageOrder / postAmount * 100)

        if percentage <= 10:
            print(f"|■---------| {percentage}%")
        elif percentage <= 20:
            print(f"|■■--------| {percentage}%")
        elif percentage <= 30:
            print(f"|■■■-------| {percentage}%")
        elif percentage <= 40:
            print(f"|■■■■------| {percentage}%")
        elif percentage <= 50:
            print(f"|■■■■■-----| {percentage}%")
        elif percentage <= 60:
            print(f"|■■■■■■----| {percentage}%")
        elif percentage <= 70:
            print(f"|■■■■■■■---| {percentage}%")
        elif percentage <= 80:
            print(f"|■■■■■■■■--| {percentage}%")
        elif percentage <= 90:
            print(f"|■■■■■■■■■-| {percentage}%")
        elif percentage <= 100:
            print(f"|■■■■■■■■■■| {percentage}%")

        extension = str(data["posts"][y]["file"]["ext"])

        try:
            # Download the image
            image_data = requests.get(fileList[y]).content
            time.sleep(1)

            with open(f"{filepath}/{imageOrder}.{extension}", 'wb') as handler:
                handler.write(image_data)

            # Save the tags to a text file
            with open(f"{filepath}/{imageOrder}.txt", "w") as f:
                f.write(", ".join(tagList[y]))

            imageOrder += 1

        except Exception as e:
            print(f"Failed to download image {imageOrder}: {e}")
            continue


        if imageOrder >= postAmount:
            break
