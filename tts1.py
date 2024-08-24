#import modules
import subprocess
import gtts
#welcome tts msg
welcomemsg="welcome to terminal voice assistant"
a1=gtts.gTTS(welcomemsg)
a1.save("tts1.mp3")
subprocess.call("mpv tts1.mp3",shell=True)
# store a color codes into class ...
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKGREEN+"welcome to text to speech termux...")
print(bcolors.OKGREEN+welcomemsg)



#command program
def repeat():
    msg=input("Enter A Command: ")
    match msg:
        case "clear":
            a=gtts.gTTS("clearing a terminal")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg,shell=True),
        case "ls":
            a=gtts.gTTS("listing a files")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg,shell=True),
            
        case "pwd":
            a=gtts.gTTS("the current location")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg,shell=True),
            
        case "sl":
            a=gtts.gTTS("sl command is running")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg,shell=True),
        case _:
            if msg!="exit":
                a=gtts.gTTS("your command "+msg+" is executing")
                a.save("tts.mp3")
                subprocess.call("mpv tts.mp3",shell=True)
    
    if msg!="exit":
        repeat()
    else:
        print(bcolors.OKGREEN+"Exit tts .....")
        msg1="closing the terminal assistant programe..."
        b=gtts.gTTS(msg1)
        b.save("tts.mp3")
        subprocess.call("mpv tts.mp3",shell=True)
repeat()

    










