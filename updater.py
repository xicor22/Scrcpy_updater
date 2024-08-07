import requests
import wget
from zipfile import ZipFile as zp
import subprocess
import os
import shutil


def download():
    url = 'https://github.com/Genymobile/scrcpy/releases/latest'
    r = requests.get(url)
    version = r.url.split('/')[-1]
    link_0 = "https://github.com/Genymobile/scrcpy/releases/latest/download/scrcpy-win64-"
    link_1 = ".zip"
    end_link = link_0+version+link_1
    final = 'C:\\Tools\\Scrcpy\\scrcpy.zip'
    wget.download(end_link, final)
    return final


def extract():
    with zp('C:\\Tools\\Scrcpy\\scrcpy.zip', 'r') as zipObj:
        zipObj.extractall('C:\\Tools\\Scrcpy')


def folder_loc():
    process = subprocess.Popen(
        ["powershell", "cd C:\\Tools\\Scrcpy\\ ; ls"], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    loc = result.decode('utf-8').split()
    folder_name = loc[14]
    return folder_name


def move(folder_name):
    des = 'C:\\Tools\\Scrcpy\\'
    fol_loc = 'C:\\Tools\\Scrcpy\\'+folder_name
    file = os.listdir(fol_loc)
    for f in file:
        src = os.path.join(fol_loc, f)
        dst = os.path.join(des, f)
        shutil.move(src, dst)
    return fol_loc


def remove(fol_loc, final):
    shutil.rmtree(fol_loc)
    os.remove(final)


def folder_check():
    folder_path = "C:\\Tools\\Scrcpy"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def main():
    folder_check()
    final = download()
    extract()
    folder_name = folder_loc()
    fol_loc = move(folder_name)
    remove(fol_loc, final)


main()
