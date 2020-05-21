### BEGIN INIT INFO
#Provides: USER GUI
#Required-Start: $remote_fs $syslog
#Required-Stop: $remote_fs $syslog
#Default-Start: 2 3 4 5
#Default-Stop: 0 1 6
#Short-Description: Start daemon at boot time
#DEscription: Enable service provided by daemon
### END INIT INFO


"""
Programmed By: Edward Ouzman
Designed for: Eyes & Ears Program
Created: 18/05/2020
"""

try:
    import tkinter as tk
    import os
    #from PIL import ImageTK,Image
except:
    import tkinter as tk
    #from PIL import ImageTK,Image
    import os

class GUIMain():
    def __init__(self):
        print(self.__InitiateInstance__())
        print(self.__ImportImages__())
        print(self.__SetBackground__())
        print(self.__GUIAddButtons__())
        self.root.lift()
        self.root.mainloop()


    def __InitiateInstance__(self):
        """creates the instance of tkinter which is required for the GUI, also sets dimensions of the window, removes the top windows bar and sets the window to always be on top"""
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('1230x400+350+300')
        self.root.wm_attributes("-topmost", True)
        return "Main GUI Window created!"


    def __SetBackground__(self):
        """Sets the Main background of the window"""
        self.background_label = tk.Label(self.root, image = self.Images["Background"])
        self.background_label.place(x=0,y=0)
        return "Background set!"


    def __GUIAddButtons__(self):
        """Creates the main different Buttons"""
        self.FirstButton = self.__CreateButton__('Internet', 55, 110, self.Images["InternetButton"])
        self.SecondButton = self.__CreateButton__('Email', 290, 110, self.Images["EmailButton"])
        self.ThirdButton = self.__CreateButton__('Contact Hub', 525, 110, self.Images["ContactHubButton"])
        self.FourthButton = self.__CreateButton__('Writing', 760, 110, self.Images["OtherButton"])
        self.ExitButton = tk.Button(self.root, text = "exit", bd = 0, image = self.Images["ExitButton"], bg = "#2C2C2C", activebackground = "#2C2C2C", command = self.__client_exit__)
        self.ExitButton.place(x = 995, y = 110, width = 180, height = 180)
        self.FourthButton.config(command = self.__otherButtonFunction__)
        self.FirstButton.config(command = self.__InternetButtonFunction__)
        self.SecondButton.config(command = self.__EmailButtonFunction__)
        return 'GUI Buttons Added!'


    def __CreateButton__(self, DisplayText, xValue, yValue, buttonImage):
        """Function to create custom Buttons"""
        ButtonObject = tk.Button(self.root, text = DisplayText, bd = 0, bg="#2C2C2C", image = buttonImage)
        ButtonObject.place(x = xValue, y = yValue, width = 180, height = 180)
        return ButtonObject
    

    def __ImportImages__(self):
        """Imports all of the images into a single images array"""
        self.Images = {}
        self.Images["InternetButton"] = tk.PhotoImage(file = 'InternetIconAttempt2.png')
        self.Images["Background"] = tk.PhotoImage(file = 'BackgroundAttempt6.png')
        self.Images["EmailButton"] = tk.PhotoImage(file = 'EmailButtonAttempt2.png')
        self.Images["BlankButton"] = tk.PhotoImage(file = 'ButtonAttempt2.png')
        self.Images["ExitButton"] = tk.PhotoImage(file = 'ExitButtonAttempt2.png')
        self.Images["ContactHubButton"] = tk.PhotoImage(file = 'ContactHubAttempt2.png')
        self.Images["OtherButton"] = tk.PhotoImage(file = 'OtherButtonAttempt3.png')
        return "Images Imported!"


    def __client_exit__(self):
        self.root.destroy()
        exit()

    def __otherButtonFunction__(self):
        self.root.destroy()
        self.newRoot = GUIMore()


    def __EmailButtonFunction__(self):

        pass


    def __InternetButtonFunction__(self):
        self.root.destroy()
        os.system('chromium-browser https://www.google.co.uk')
        os.system('python3 EyesGUI.py')
        exit()

class GUIMore():
    """This window consists of the additional buttons, options and settings not available on the first page"""
    def __init__(self):
        print(self.__CreateInstance__())
        print(self.__ImportImages__())
        print(self.__SetBackground__())
        print(self.__GUIAddButtons__())

    def __CreateInstance__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('1230x800+125+60')
        return "Created Seconary Instance Window"


    def __ImportImages__(self):
        self.Images = {}
        self.Images["Background"] = tk.PhotoImage(file = 'SecondaryBackgroundAttempt1.png')
        self.Images["Blank Button"] = tk.PhotoImage(file = 'ButtonAttempt2.png')
        return "Images Imported!"


    def __SetBackground__(self):
        self.Background_label = tk.Label(self.root, image = self.Images["Background"])
        self.Background_label.place(x=0, y=0)
        self.Background_label.bind('<Button-1>', self.__BackToMain__)
        return "Background image set!"

    def __CreateButton__(self, DisplayText, xValue, yValue, buttonImage):
        """Function to create custom Buttons"""
        ButtonObject = tk.Button(self.root, text = DisplayText, bd = 0, bg="#2C2C2C", image = buttonImage)
        ButtonObject.place(x = xValue, y = yValue, width = 180, height = 180)
        return ButtonObject

    def __GUIAddButtons__(self):
        self.Buttons = {}
        self.FirstRowHeight = 170
        self.SecondRowHeight = 405
        self.Buttons["1.0"] = self.__CreateButton__("Button", 55, self.FirstRowHeight, self.Images["Blank Button"])
        self.Buttons["1.1"] = self.__CreateButton__("Button", 290, self.FirstRowHeight, self.Images["Blank Button"])
        self.Buttons["1.2"] = self.__CreateButton__("Button", 525, self.FirstRowHeight, self.Images["Blank Button"])
        self.Buttons["1.3"] = self.__CreateButton__("Button", 760, self.FirstRowHeight, self.Images["Blank Button"])
        self.Buttons["1.4"] = self.__CreateButton__("Button", 995, self.FirstRowHeight, self.Images["Blank Button"])
        self.Buttons["2.0"] = self.__CreateButton__("Button", 55, self.SecondRowHeight, self.Images["Blank Button"])
        self.Buttons["2.1"] = self.__CreateButton__("Button", 290, self.SecondRowHeight, self.Images["Blank Button"])
        self.Buttons["2.2"] = self.__CreateButton__("Button", 525, self.SecondRowHeight, self.Images["Blank Button"])
        self.Buttons["2.3"] = self.__CreateButton__("Button", 760, self.SecondRowHeight, self.Images["Blank Button"])
        self.Buttons["2.4"] = self.__CreateButton__("Button", 995, self.SecondRowHeight, self.Images["Blank Button"])
        return "Added Buttons"


    def __BackToMain__(self, som):
        self.root.destroy()
        self.newRoot = GUIMain()
        return "Returned to Main"


if __name__ == "__main__":
    """Where the application starts"""
    root = GUIMain()

