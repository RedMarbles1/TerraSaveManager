# TerraSaveManager
A tool to make Terraria load saves from a different folder using symlinks.

## Requirements
Python 3.10 or above

## How to use
First edit the script and change the linkdir variable at the top to whatever directory you want Terraria to save to now. Copy your Terraria save data to this folder.
Then run the script and follow the instructions. If you are on Windows you should run it as administrator.

## iOS Shortcuts Setup
Oh yeah we got this working on iOS now

I don't have an android device to test so until someone sends me a method you guys are on your own sorryyyy

To get your iOS Terraria saves to sync with your PC you can use these instructions:
First of all, download iCloud on your PC if you are on Windows. macOS users don't have to do anything here. I don't know if any iCloud app exists for linux so linux users are kinda on their own.

Then create a folder somewhere in your iCloud Drive and use that folder as the linkdir variable for the script to link it.

Here is where the fun part begins:

Download these 2 shortcuts to your iOS device:

TSM App Open Shortcut:

https://www.icloud.com/shortcuts/5c6b36432efe4f749bc5ce5ddef55a81

TSM App Close Shortcut:

https://www.icloud.com/shortcuts/6d8c0d3e4da347c0a1990da01cc7dbe6

When you are done with the downloads, go to your automations page on the shortcuts app and create a new personal automation. From there, select App. Then, select Terraria as the app and select only Is Opened and select "Run Immediately". THen search for TSM App Open shortcut and select that. Do this again but select only Is Closed and TSM App Close Shortcut. You should now be able to sync your saves between iOS and PC!


