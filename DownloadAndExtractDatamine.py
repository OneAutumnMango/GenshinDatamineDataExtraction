import urllib.request
import zipfile
import os
import shutil

from datetime import datetime

def download():
    url = "https://github.com/Dimbreath/GenshinData/archive/refs/heads/master.zip"
    print ("Downloading...")
    print(datetime.now().time())
    filename, headers = urllib.request.urlretrieve(url, filename="./DimbreathDatamine.zip")
    print ("Download complete!")
    print(datetime.now().time())

def unzip():
    if os.path.exists("./DimbreathDatamine.zip"):
        print("\nUnzipping...")
        print(datetime.now().time())
        with zipfile.ZipFile("./DimbreathDatamine.zip", 'r') as zip_ref:
            try:
                zip_ref.extractall("./DimbreathDatamine")
            except FileNotFoundError:
                print(
"""Error: FileNotFoundError
                
Please do not tamper with the files mid download.
Run this program again to fix it.""")
                input("\n\nPress Enter to Exit")
                exit()
        print("Unzipped!")
        print(datetime.now().time())
    else: 
        print("No file to UNZIP.")

def delZIP():
    print("\nRemoving ZIP...")
    print(datetime.now().time())
    if os.path.exists("./DimbreathDatamine.zip"):
        os.remove("./DimbreathDatamine.zip")
        print("Zip removed!")
        print(datetime.now().time())
    else: 
        print("No ZIP file to delete.")

def moveAndDelExtra():
    print("\nRemoving extra files...")
    print(datetime.now().time())
    if os.path.exists(".\DimbreathDatamine\GenshinData-master"):
        try:
            shutil.rmtree(".\DimbreathDatamine\ExcelBinOutput", ignore_errors=True)
            shutil.move(".\DimbreathDatamine\GenshinData-master\ExcelBinOutput",".\DimbreathDatamine")
        except:
            print(
"""Ignoring Errors AHHHHHHHHHHHHH!!!!!!!!!
            
Lowkey though, run the file again to fix :).
            
Error: shutil.Error:Destination not found.""")
            input("\n\nPress Enter to Exit")
            exit()
            
        shutil.rmtree(".\DimbreathDatamine\GenshinData-master", ignore_errors=True)
        print("Extra files removed!")
    else:
        print("No extra files found.")
    print(datetime.now().time())
    print("\nFile Extraction Complete!")

download()
unzip()
delZIP()
moveAndDelExtra()


input("\n\nPress Enter to Exit")
exit()