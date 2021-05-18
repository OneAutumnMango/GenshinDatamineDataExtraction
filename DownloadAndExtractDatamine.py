import urllib.request
import zipfile
import os
import shutil

from datetime import datetime

url = "https://github.com/Dimbreath/GenshinData/archive/refs/heads/master.zip"


print ("Downloading...")
print(datetime.now().time())
filename, headers = urllib.request.urlretrieve(url, filename="./DimbreathDatamine.zip")
print ("Download complete!")
print(datetime.now().time())

if os.path.exists("./DimbreathDatamine.zip"):
    print("\nUnzipping...")
    print(datetime.now().time())
    with zipfile.ZipFile("./DimbreathDatamine.zip", 'r') as zip_ref:
        zip_ref.extractall("./DimbreathDatamine")
    print("Unzipped!")
    print(datetime.now().time())
else: 
    print("No file to UNZIP.")

print("\nRemoving ZIP...")
print(datetime.now().time())
if os.path.exists("./DimbreathDatamine.zip"):
    os.remove("./DimbreathDatamine.zip")
    print("Zip removed")
    print(datetime.now().time())
else: 
    print("No ZIP file to delete.")

print("\nRemoving extra files...")
print(datetime.now().time())
if os.path.exists(".\DimbreathDatamine\GenshinData-master"):
    try:
        shutil.move(".\DimbreathDatamine\GenshinData-master\ExcelBinOutput",".\DimbreathDatamine")
    except:
        pass
    shutil.rmtree(".\DimbreathDatamine\GenshinData-master", ignore_errors=True)
    print("Extra files removed")
else:
    print("No extra files found")
print(datetime.now().time())
print("\nFile Extraction Complete")
input("\n\nPress Enter to Exit")