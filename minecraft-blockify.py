import requests
import os
import colorama
from colorama import Fore, Style

blockified = 0

print("What is your desired max height and width in blocks? (Enter 0 for none)")
print("")


while True:
  try:
    maxh = int(input("Height: "))
  except ValueError:
    print(Fore.RED + "The max height has to be 0 or more. Please enter your desired max height in blocks. (Enter 0 for none)" + Fore.WHITE)
    continue
  if maxh < 0:
    print(Fore.RED + "The max height has to be 0 or more. Please enter your desired max height in blocks. (Enter 0 for none)" + Fore.WHITE)
    continue
  else:
    break

if maxh > 0:
  maxh = "&MaxHeight=" + str(maxh)
elif maxh == 0:
  maxh = None

while True:
  try:
    maxw = int(input("Width: "))
  except ValueError:
    print(Fore.RED + "The max width has to be 0 or more. Please enter your desired max height in blocks. (Enter 0 for none)" + Fore.WHITE)
    continue
  if maxw < 0:
    print(Fore.RED + "The max width has to be 0 or more. Please enter your desired max height in blocks. (Enter 0 for none)" + Fore.WHITE)
    continue
  else:
    break

if maxw > 0:
  maxw = "&MaxHeight=" + str(maxw)
elif maxw == 0:
  maxh = None


print("")
print("What is your desired output format?")
print("")
print("1: JPEG (Not transparent)")
print("2: PNG (Transparent)")
oformat = int(input("Pick your answer 1 or 2: "))
print("")

if oformat == 1:
  oformat = "jpeg"
elif oformat == 2:
  oformat = "png"
else:
  oformat = int(input(Fore.RED + "The chosen format is not valid. Please chose 1 or 2: " + Fore.WHITE))

if oformat is not None:
  if os.path.isfile("input.txt") == False:
    print(Fore.RED + 'You have not added any links to "input.txt". Please add your links to "input.txt" and restart this script.')
    file = open("input.txt", "w")
    file.close()
  file = open("input.txt", "r")
  line_count = 0
  for line in file:
    if line != "\n":
        line_count += 1
  if line_count == 0:
    print(Fore.RED + 'You have not added any links to "input.txt". Please add your links to "input.txt" and restart this script.')
  else:
    if os.path.exists("output") == False:
      os.makedirs("output")
  file = open("input.txt", "r")
  for line in file:
    response = requests.get("""https://taylorlove.info/projects/pixelstacker/api/Render/ByURLAdvanced?Url=""" + line + """&Format=""" + oformat + "&IsMultiLayer=false" + str(maxh) + str(maxw))
    blockified = blockified + 1
    file = open("output/" + str(blockified) + "." + oformat, "wb")
    file.write(response.content)
    file.close()
    print("Line " + str(blockified) + " has been blockified ("+ str(blockified) + "/" + str(line_count) + ")")