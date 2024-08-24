#import modules
import subprocess
import gtts
import time
#welcome tts msg
welcomemsg="welcome to terminal voice assistant"
a1=gtts.gTTS(welcomemsg)
a1.save("tts1.mp3")
subprocess.call("mpv tts1.mp3",shell=True)
print("welcome to text to speech termux...")

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
        print("Exit tts .....")
        msg1="closing the terminal assistant programe..."
        b=gtts.gTTS(msg1)
        b.save("tts.mp3")
        subprocess.call("mpv tts.mp3",shell=True)
repeat()

    










