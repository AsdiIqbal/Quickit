'''
This code and GUI design in not final yet.
It is made ready for testing only.

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget ,QMainWindow, QSizePolicy, QDesktopWidget, QButtonGroup
from PyQt5 import uic
import string


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FrontEnd.ui",self)
        self.btn_count=0
        
        # Configuring All Button

        # List of all motor modules buttons 
        self.module_btns=[
            (self.M1Btn, self.M1Page), (self.M2Btn, self.M2Page), (self.M3Btn,  self.M3Page), (self.M4Btn,  self.M4Page),
            (self.M5Btn,  self.M5Page), (self.M6Btn,  self.M6Page), (self.M7Btn,  self.M7Page), (self.M8Btn,  self.M8Page),
            (self.M9Btn,  self.M9Page), (self.M10Btn,  self.M10Page), (self.M11Btn,  self.M11Page), (self.M12Btn,  self.M12Page),
            (self.M13Btn,  self.M13Page), (self.M14Btn,  self.M14Page), (self.M15Btn,  self.M15Page), (self.M16Btn,  self.M16Page) 
            ]
        

        # List of All Pages
        self.Screen_btns = [
            (self.HomeBtn,self.HomePage), (self.TeachPendantBtn,self.TeachPendantPage),
            (self.CodeBtn,self.CodePage), (self.SettingsBtn,self.SettingsPage)
        ]
        
        # List of all Modules Parameter Manipulators
        self.MpageContent =  [
            [[self.M1AngleLabel, self.M1AnglePlus, self.M1AngleMinus, self.M1AngleSlider], [self.M1VelocityLabel, self.M1VelocityPlus, self.M1VelocityMinus, self.M1VelocitySlider]],
            [[self.M2AngleLabel, self.M2AnglePlus, self.M2AngleMinus, self.M2AngleSlider], [self.M2VelocityLabel, self.M2VelocityPlus, self.M2VelocityMinus, self.M2VelocitySlider]],
            [[self.M3AngleLabel, self.M3AnglePlus, self.M3AngleMinus, self.M3AngleSlider], [self.M3VelocityLabel, self.M3VelocityPlus, self.M3VelocityMinus, self.M3VelocitySlider]],
            [[self.M4AngleLabel, self.M4AnglePlus, self.M4AngleMinus, self.M4AngleSlider], [self.M4VelocityLabel, self.M4VelocityPlus, self.M4VelocityMinus, self.M4VelocitySlider]],
            [[self.M5AngleLabel, self.M5AnglePlus, self.M5AngleMinus, self.M5AngleSlider], [self.M5VelocityLabel, self.M5VelocityPlus, self.M5VelocityMinus, self.M5VelocitySlider]],
            [[self.M6AngleLabel, self.M6AnglePlus, self.M6AngleMinus, self.M6AngleSlider], [self.M6VelocityLabel, self.M6VelocityPlus, self.M6VelocityMinus, self.M6VelocitySlider]],
            [[self.M7AngleLabel, self.M7AnglePlus, self.M7AngleMinus, self.M7AngleSlider], [self.M7VelocityLabel, self.M7VelocityPlus, self.M7VelocityMinus, self.M7VelocitySlider]],
            [[self.M8AngleLabel, self.M8AnglePlus, self.M8AngleMinus, self.M8AngleSlider], [self.M8VelocityLabel, self.M8VelocityPlus, self.M8VelocityMinus, self.M8VelocitySlider]],
            [[self.M9AngleLabel, self.M9AnglePlus, self.M9AngleMinus, self.M9AngleSlider], [self.M9VelocityLabel, self.M9VelocityPlus, self.M9VelocityMinus, self.M9VelocitySlider]],
            [[self.M10AngleLabel, self.M10AnglePlus, self.M10AngleMinus, self.M10AngleSlider], [self.M10VelocityLabel, self.M10VelocityPlus, self.M10VelocityMinus, self.M10VelocitySlider]],
            [[self.M11AngleLabel, self.M11AnglePlus, self.M11AngleMinus, self.M11AngleSlider], [self.M11VelocityLabel, self.M11VelocityPlus, self.M11VelocityMinus, self.M11VelocitySlider]],
            [[self.M12AngleLabel, self.M12AnglePlus, self.M12AngleMinus, self.M12AngleSlider], [self.M12VelocityLabel, self.M12VelocityPlus, self.M12VelocityMinus, self.M12VelocitySlider]],
            [[self.M13AngleLabel, self.M13AnglePlus, self.M13AngleMinus, self.M13AngleSlider], [self.M13VelocityLabel, self.M13VelocityPlus, self.M13VelocityMinus, self.M13VelocitySlider]],
            [[self.M14AngleLabel, self.M14AnglePlus, self.M14AngleMinus, self.M14AngleSlider], [self.M14VelocityLabel, self.M14VelocityPlus, self.M14VelocityMinus, self.M14VelocitySlider]],
            [[self.M15AngleLabel, self.M15AnglePlus, self.M15AngleMinus, self.M15AngleSlider], [self.M15VelocityLabel, self.M15VelocityPlus, self.M15VelocityMinus, self.M15VelocitySlider]],
            [[self.M16AngleLabel, self.M16AnglePlus, self.M16AngleMinus, self.M16AngleSlider], [self.M16VelocityLabel, self.M16VelocityPlus, self.M16VelocityMinus, self.M16VelocitySlider]]
        ]

        # List of All Modules Status Views
        self.Module_Labels = {
        "M1" : self.M1Status, "M2" : self.M2Status, "M3" : self.M3Status, "M4" : self.M4Status,
        "M5" : self.M5Status, "M6" : self.M6Status, "M7" : self.M7Status, "M8" : self.M8Status,
        "M9" : self.M9Status, "M10" : self.M10Status, "M11" : self.M11Status, "M12" : self.M12Status,
        "M13" : self.M13Status, "M14" : self.M14Status, "M15" : self.M15Status, "M16" : self.M16Status, 
        } 
        '''
        Dictionary of all Module Values
        Extract data at any instant
        This is what you need to parse to serialize it to Arduino IDE
        just call this method from outside of the class
        | | |  
        v v v     '''
        self.Module_Status = {k:v.text() for  k,v in self.Module_Labels.items()}



        for i in self.module_btns:
            i[0].clicked.connect(self.changeMpages)

        for i in self.Screen_btns:
            i[0].clicked.connect(self.changepages)
        
        for i in self.MpageContent:
            i[0][1].clicked.connect(self.slideplus)
            i[0][2].clicked.connect(self.slideminus)
            i[1][1].clicked.connect(self.slideplus)
            i[1][2].clicked.connect(self.slideminus)
            i[0][3].valueChanged.connect(self.tweek)
            i[1][3].valueChanged.connect(self.tweek)

        self.HomeScreens.setCurrentWidget(self.HomePage)
        self.MotorControlPages.setCurrentWidget(self.MainControlPage)
        
    def tweek(self):
        btn=self.sender()
        for i in self.MpageContent:
            for j in i:
                if j[3] is btn:
                    value = j[3].value()
                    j[0].setText(f"{value}")
            for k,v in self.Module_Labels.items():
                if k[1:] == "".join([j for j in i[0][0].objectName() if j not in string.ascii_letters]):
                    v.setText(f"({i[0][0].text()},{i[1][0].text()})")
   
    def changepages(self):
        btn = self.sender()
        for i  in self.Screen_btns:
            if i[0] is btn:
                self.HomeScreens.setCurrentWidget(i[1])
                
    def changeMpages(self):
        btn = self.sender()
        for i  in self.module_btns:
            if i[0] is btn:
                self.MotorControlPages.setCurrentWidget(i[1])
                
    def slideplus(self):
        inc = 10
        btn=self.sender()
        for i in self.MpageContent:
            for j in i:
                if j[1] is btn:
                    value = j[3].value()
                    j[3].setValue(value+inc)
                    j[0].setText(f"{j[3].value()}")
        
    def slideminus(self):
        inc = 10
        btn=self.sender()
        for i in self.MpageContent:
            for j in i:
                if j[2] is btn:
                    value = j[3].value()
                    j[3].setValue(value-inc)
                    j[0].setText(f'{j[3].value()}')
                    
            


if __name__ == "__main__":
    app=QApplication([])          
    app.setStyle("Fusion") 
    obj=Window()                  
    print("Done successfully")
    obj.show()                     
    sys.exit(app.exec())