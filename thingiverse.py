import requests
import threading, queue
import os
import time
from bs4 import BeautifulSoup
import io
import zipfile
import shutil
from termcolor import colored

root = input(colored("Enter the path to the root folder (if exists, it will be emptied first; otherwise, it will be automatically created: ", "yellow"))

if os.path.exists(root):
  ok = input(colored(" • The entered directory already contains files.\n • If you continue, these files will be automatically deleted to initially clear the specified directory.\n • If you understand and want to continue, enter [Y], otherwise, enter [N]: ", "red"))
  while not (ok == "Y" or ok == "N"):
    if ok == "Y":
      shutil.rmtree(root)
      break
    elif ok == "N":
      break
    else:
      ok = input(colored("Invalid. Please enter either [Y] or [N] (don't actually type the brackets): ", "yellow"))
  
  if ok == "N":
    exit()

os.mkdir(root)
os.mkdir(root + "files/")

n = 0
urls = []

def worker():
  global n, urls

  while True:
    number = q.get()
    url = "https://www.thingiverse.com/thing:{}/zip".format(number)

    if not url in urls:
      urls.append(url)

      while True:
        try:
          r = requests.get(url)
        except:
          time.sleep(1.0)
          continue
        break

      if r.status_code == 200:
        with open(root + "thingiverse.txt", "a") as f:
          f.write(str(number))
        f.close()

        buffer = r.content
        zip = zipfile.ZipFile(io.BytesIO(buffer))
        name_list = zip.namelist()
        indices = [i for i, name in enumerate(name_list) if '.stl' in name.lower()]
      
        for index in indices:
          zip.extract(name_list[index], root + "files/")
          n += 1
          print (n, end = "\r")

        zip.close()
     
    q.task_done()

q = queue.Queue()

for i in range(256):
  threading.Thread(target = worker).start()

for number in range(1000000, 9999999):
  q.put(number)

q.join()
