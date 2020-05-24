#REMOTEACCESSSUCCESS!!!
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
    import threading
    #from PIL import ImageTK,Image
except:
    import tkinter as tk
    #from PIL import ImageTK,Image
    import os
    import threading

class ThreadedInstance():
    def __init__(self, command):
        self.ThreadingCommand = lambda: os.system('{}'.format(command))
        self.Thread = threading.Thread(target = self.ThreadingCommand)
        self.Thread.start()

class GUILocate():
    """Creates a small window in the bottom of the screen when the GUI is closed so the user can reopen the GUI easily"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.i = ImportImages("Return")
        self.root.geometry("100x100+{}+{}".format(str(setup.DimensionsX-100), str(setup.DimensionsY-100)))
        self.ReturnButton = tk.Button(self.root, text = "Reutrn to GUI", image = self.i.Images["ReturnGUI"])
        self.ReturnButton.place(x = 0, y = 0, width = 100, height = 100)
        self.ReturnButton.config(command = self.__clientExit__)
        self.root.mainloop()

    def __clientExit__(self):
        self.root.destroy()
        os.system('pkill chromium')
        os.system('pkill abiword')

class Setup():
    """Gets the dimensions of the screen, sets the size of the GUI Windows in pixels"""
    def __init__(self):
        self.DimensionsRaw = os.popen('fbset -s').read()
        self.DimensionsClean = self.DimensionsRaw.split("\"")[1]
        self.DimensionsX = (int(int(self.DimensionsClean.split("x")[0])))
        self.DimensionsY = (int(int(self.DimensionsClean.split("x")[1])))
        self.WindowSize = ""

        if self.DimensionsX < 1000:
            self.WindowSize = "small"
            self.GUIX = 615
            self.GUIY1 = 200
            self.GUIY2 = 400
            self.GUIButtonSize = 90

        elif self.DimensionsX < 2560:
            self.WindowSize = "regular"
            self.GUIX = 1230
            self.GUIY1 = 400
            self.GUIY2 = 800
            self.GUIButtonSize = 180
            self.ButtonPositionsX = []
            self.PositionCounter = 55
            for x in range(0,5):
                self.ButtonPositionsX.append(self.PositionCounter)
                self.PositionCounter += 235
            self.RowHeightMain = 110
            self.RowHeightSecondary1 = 170
            self.RowHeightSecondary2 = 405
        else:
            self.WindowSize = "Large"
            self.GUIX = 1845
            self.GUIY1 = 600
            self.GUIY2 = 1200
            self.GUIButtonSize = 270

class ImportImages():
    def __init__(self, importWhat):
        self.importWhat = importWhat
        self.SmallImagePath = '/home/pi/EyesGUI-master/SmallImg/'
        self.RegularImagePath = '/home/pi/EyesGUI-master/RegImg/'
        self.LargeImagePath = '/home/pi/EyesGUI-master/LargeImg/'
        if setup.WindowSize == "small":
            self.__import__(self.SmallImagePath, self.importWhat)
        elif setup.WindowSize == "regular":
            self.__import__(self.RegularImagePath, self.importWhat)
        else:
            self.__import__(self.LargeImagePath, self.importWhat)

    def __import__(self, SizePath, importWhat):
        self.Images = {}
        if importWhat == "primary":
            self.Images["InternetButton"] = tk.PhotoImage(file = '{}InternetIconAttempt2.png'.format(SizePath))
            self.Images["Background Regular GUI"] = tk.PhotoImage(file = '{}BackgroundAttempt8.png'.format(SizePath))
            self.Images["EmailButton"] = tk.PhotoImage(file = '{}EmailButtonAttempt2.png'.format(SizePath))
            self.Images["ExitButton"] = tk.PhotoImage(file = '{}ExitButtonAttempt2.png'.format(SizePath))
            self.Images["ContactHubButton"] = tk.PhotoImage(file = '{}ContactHubAttempt2.png'.format(SizePath))
            self.Images["OtherButton"] = tk.PhotoImage(file = '{}OtherButtonAttempt3.png'.format(SizePath))
        elif importWhat == "secondary":
            self.Images["Background Large GUI"] = tk.PhotoImage(file = '{}SecondaryBackgroundAttempt2.png'.format(SizePath))
            self.Images["BlankButton"] = tk.PhotoImage(file = '{}ButtonAttempt2.png'.format(SizePath))
            self.Images["WeatherButton"] = tk.PhotoImage(file = '{}WeatherButtonAttempt1.png'.format(SizePath))
            self.Images["NewsButton"] = tk.PhotoImage(file = '{}NewsButtonAttempt1.png'.format(SizePath))
            self.Images["ReturnButton"] = tk.PhotoImage(file = '{}ReturnButtonAttempt1.png'.format(SizePath))
            self.Images["FacebookButton"] = tk.PhotoImage(file = '{}FacebookButtonAttempt1.png'.format(SizePath))
            self.Images["MentalHealthButton"] = tk.PhotoImage(file = '{}MentalHealthButtonAttempt1.png'.format(SizePath))
            self.Images["WordButton"] = tk.PhotoImage(file = '{}WordButtonAttempt1.png'.format(SizePath))
        elif importWhat == "Return":
            self.Images["ReturnGUI"] = tk.PhotoImage(file = '{}ReturnButtonGUIAttempt1.png'.format(SizePath))
        return "Imported Images!"

class GUIMain():
    def __init__(self):
        print(self.__InitiateInstance__())
        self.i = ImportImages("primary")
        print(self.__SetBackground__())
        print(self.__GUIAddButtons__())
        self.root.lift()
        self.root.mainloop()


    def __InitiateInstance__(self):
        """creates the instance of tkinter which is required for the GUI, also sets dimensions of the window, removes the top windows bar and sets the window to always be on top"""
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('{}x{}+{}+{}'.format(str(setup.GUIX), str(setup.GUIY1), str(int(setup.DimensionsX/2)-615), str(int(setup.DimensionsY/2)-200)))
        self.root.wm_attributes("-topmost", True)
        return "Main GUI Window created!"


    def __SetBackground__(self):
        """Sets the Main background of the window"""
        self.background_label = tk.Label(self.root, image = self.i.Images["Background Regular GUI"])
        self.background_label.place(x=0,y=0)
        return "Background set!"


    def __GUIAddButtons__(self):
        """Creates the main different Buttons"""
        self.FirstButton = self.__CreateButton__('Internet', setup.ButtonPositionsX[0], setup.RowHeightMain, self.i.Images["InternetButton"])
        self.SecondButton = self.__CreateButton__('Email', setup.ButtonPositionsX[1], setup.RowHeightMain, self.i.Images["EmailButton"])
        self.ThirdButton = self.__CreateButton__('Contact Hub', setup.ButtonPositionsX[2], setup.RowHeightMain, self.i.Images["ContactHubButton"])
        self.FourthButton = self.__CreateButton__('Writing', setup.ButtonPositionsX[3], setup.RowHeightMain, self.i.Images["OtherButton"])
        self.ExitButton = self.__CreateButton__('Exit Button', setup.ButtonPositionsX[4], setup.RowHeightMain, self.i.Images["ExitButton"])
        self.ExitButton.config(command = self.__client_exit__)
        self.FourthButton.config(command = self.__otherButtonFunction__)
        self.FirstButton.config(command = self.__InternetButtonFunction__)
        self.SecondButton.config(command = self.__EmailButtonFunction__)
        return 'GUI Buttons Added!'


    def __CreateButton__(self, DisplayText, xValue, yValue, buttonImage):
        """Function to create custom Buttons"""
        ButtonObject = tk.Button(self.root, text = DisplayText, bd = 0, bg="#2C2C2C", image = buttonImage)
        ButtonObject.place(x = xValue, y = yValue, width = setup.GUIButtonSize, height = setup.GUIButtonSize)
        return ButtonObject



    def __client_exit__(self):
        self.root.destroy()

    def __otherButtonFunction__(self):
        self.root.destroy()
        self.newRoot = GUIMore()


    def __EmailButtonFunction__(self):
        self.root.destroy()
        self.EmailCommand = ThreadedInstance('lxterminal -e chromium-browser --start-fulscreen www.gmail.com')


    def __InternetButtonFunction__(self):
        self.root.destroy()
        self.InternetCommand = ThreadedInstance('lxterminal -e chromium-browser --start-fullscreen https://www.google.com')

class GUIMore():
    """This window consists of the additional buttons, options and settings not available on the first page"""
    def __init__(self):
        print(self.__CreateInstance__())
        self.i = ImportImages("secondary")
        print(self.__SetBackground__())
        print(self.__GUIAddButtons__())

    def __CreateInstance__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('{}x{}+{}+{}'.format(str(setup.GUIX), str(setup.GUIY2), str(int(setup.DimensionsX/2)-615), str(int(setup.DimensionsY/2)-400)))
        return "Created Seconary Instance Window"


    def __SetBackground__(self):
        self.Background_label = tk.Label(self.root, image = self.i.Images["Background Large GUI"])
        self.Background_label.place(x=0, y=0)
        return "Background image set!"

    def __CreateButton__(self, DisplayText, xValue, yValue, buttonImage):
        """Function to create custom Buttons"""
        ButtonObject = tk.Button(self.root, text = DisplayText, bd = 0, bg="#2C2C2C", image = buttonImage)
        ButtonObject.place(x = xValue, y = yValue, width = setup.GUIButtonSize, height = setup.GUIButtonSize)
        return ButtonObject

    def __GUIAddButtons__(self):
        self.Buttons = {}
        self.FirstRowHeight = 170
        self.SecondRowHeight = 405
        self.Buttons["1.0"] = self.__CreateButton__("News", setup.ButtonPositionsX[0], self.FirstRowHeight, self.i.Images["NewsButton"])
        self.Buttons["1.1"] = self.__CreateButton__("Weather", setup.ButtonPositionsX[1], self.FirstRowHeight, self.i.Images["WeatherButton"])
        self.Buttons["1.2"] = self.__CreateButton__("Facebook", setup.ButtonPositionsX[2], self.FirstRowHeight, self.i.Images["FacebookButton"])
        self.Buttons["1.3"] = self.__CreateButton__("Word", setup.ButtonPositionsX[3], self.FirstRowHeight, self.i.Images["WordButton"])
        self.Buttons["1.4"] = self.__CreateButton__("Button", setup.ButtonPositionsX[4], self.FirstRowHeight, self.i.Images["BlankButton"])
        self.Buttons["2.0"] = self.__CreateButton__("Button", setup.ButtonPositionsX[0], self.SecondRowHeight, self.i.Images["BlankButton"])
        self.Buttons["2.1"] = self.__CreateButton__("Button", setup.ButtonPositionsX[1], self.SecondRowHeight, self.i.Images["BlankButton"])
        self.Buttons["2.2"] = self.__CreateButton__("Mental Health", setup.ButtonPositionsX[2], self.SecondRowHeight, self.i.Images["MentalHealthButton"])
        self.Buttons["2.3"] = self.__CreateButton__("Button", setup.ButtonPositionsX[3], self.SecondRowHeight, self.i.Images["BlankButton"])
        self.Buttons["2.4"] = self.__CreateButton__("Return", setup.ButtonPositionsX[4], self.SecondRowHeight, self.i.Images["ReturnButton"])
        self.Buttons["1.1"].config(command = self.__WeatherButton__)
        self.Buttons["1.0"].config(command = self.__NewsButton__)
        self.Buttons["2.4"].config(command = self.__BackToMain__)
        self.Buttons["1.2"].config(command = self.__OpenFacebook__)
        self.Buttons["1.3"].config(command = self.__OpenWord__)
        return "Added Buttons"

    def __WeatherButton__(self):
        self.root.destroy()
        self.WeatherButton = ThreadedInstance('lxterminal -e chromium-browser --start-fullscreen https://www.bbc.co.uk/weather')

    def __NewsButton__(self):
        self.root.destroy()
        self.NewsButton = ThreadedInstance('lxterminal -e chromium-browser --start-fullscreen https://www.bbc.co.uk/news')

    def __OpenFacebook__(self):
        self.root.destroy()
        self.FacebookButton = ThreadedInstance('lxterminal -e chromium-browser --start-fullscreen https://www.facebook.com')

    def __OpenWord__(self):
        self.root.destroy()
        self.WordButton = ThreadedInstance('lxterminal -e abiword -g {}'.format(setup.DimensionsClean))

    def __BackToMain__(self):
        self.root.destroy()
        self.newRoot = GUIMain()
        return "Returned to Main"

class Settings():
    def __init__(self):
        self.FileName = "/home/pi/EyesGUI-master/settings.txt"
        with open(self.FileName) as f:
            self.raw = f.readlines()
        print(self.raw)
"""
        if self.raw[0] == "settings\n":
            #FORM FOR USER SETTINGS GOES HERE
            self.root = tk.Tk()
            self.root.geometry('1230x800+{}+{}'.format(str(int(setup.DimensionsX/2)-615), str(int(setup.DimensionsY/2)-400)))
            self.root.overrideredirect(True)
            #self.root.mainloop()
        else:
            #asign the values for different settings here
            pass
"""

if __name__ == "__main__":
    """Where the application starts"""
    setup = Setup()
    settings = Settings()
    while True:
        root = GUIMain()
        side = GUILocate()
