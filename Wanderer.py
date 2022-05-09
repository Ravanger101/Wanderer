import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")
    
typingPrint("Hello world...\n")
time.sleep(1)
typingPrint("Hmmm... Anybody here?\n")
time.sleep(1)

pillColor = typingInput(" Yes or No...")

if pillColor == "Yes":
  typingPrint("Oh I thought, no one was here. I am Python a Simple Computer Language.\n")
  typingPrint("Well I got to go and handle the Computer...\n")
elif pillColor == "No":
  typingPrint("Python Is Alone\n")
else:
  typingPrint("Invalid answer!\n")

time.sleep(1)  
typingPrint("Good bye!\n")
typingPrint("This screen will clear itself in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)
clearScreen()