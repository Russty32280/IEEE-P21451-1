#Author: Tom Morris, Brian Finch, Russell Trafford
#Date: 10.30.2014
#Description: This code is a GUI for a vTEDS reader/writer. (IEEE1451-4)

#------------------------------------------------------Import Libraries--------------------------------------------------------
import sys
import os.path
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import xml.etree.ElementTree as ET
import urllib2


#------------------------------------------------SG_vTEDS Global Variables-------------------------------------------------
#GUI Global Widgets
global SG_vTEDS                              #main frame
global SGvTEDS_TitleLabel             #main frame - Title Label

global SGVTEDSMenu                     #main frame - Menu bar
global SGvTEDSMenu_File                                  #Menu Bar - File Option
global SGvTEDSMenu_Reference                         #Menu Bar - Reference Option
global SGvTEDSMenu_Help                                #Menu Bar - Help Option

global Basic_ManufacturerID_Entry  #main frame - basic TEDS
global Basic_ModelNumber_Entry     #main frame - basic TEDS
global Basic_VersionLetter_Entry      #main frame - basic TEDS
global Basic_VersionNumber_Entry   #main frame - basic TEDS
global Basic_SerialNumber_Entry      #main frame - basic TEDS
global SaveAs_Entry                            #main frame - save TEDS
global RequestTEDS_Entry            # Used in determining URL based requests for TEDS

global ExtendedTEDS_Options         #Template select option array
global ExtendedTemplate_Option     #main frame - extended TEDS option menu

global Extended1_Label                  #main frame - extended TEDS
global Extended1_Entry                  #main frame - extended TEDS
global Extended2_Label                  #main frame - extended TEDS
global Extended2_Entry                  #main frame - extended TEDS
global Extended3_Label                  #main frame - extended TEDS
global Extended3_Entry                  #main frame - extended TEDS
global Extended4_Label                  #main frame - extended TEDS
global Extended4_Entry                  #main frame - extended TEDS
global Extended5_Label                  #main frame - extended TEDS
global Extended5_Entry                  #main frame - extended TEDS
global Extended6_Label                  #main frame - extended TEDS
global Extended6_Entry                  #main frame - extended TEDS
global Extended7_Label                  #main frame - extended TEDS
global Extended7_Entry                  #main frame - extended TEDS
global Extended8_Label                  #main frame - extended TEDS
global Extended8_Entry                  #main frame - extended TEDS
global Extended9_Label                  #main frame - extended TEDS
global Extended9_Entry                  #main frame - extended TEDS
global Extended10_Label                  #main frame - extended TEDS
global Extended10_Entry                  #main frame - extended TEDS
global Extended11_Label                  #main frame - extended TEDS
global Extended11_Entry                  #main frame - extended TEDS
global Extended12_Label                  #main frame - extended TEDS
global Extended12_Entry                  #main frame - extended TEDS
global Extended13_Label                  #main frame - extended TEDS
global Extended13_Entry                  #main frame - extended TEDS
global Extended14_Label                  #main frame - extended TEDS
global Extended14_Entry                  #main frame - extended TEDS
global Extended15_Label                  #main frame - extended TEDS
global Extended15_Entry                  #main frame - extended TEDS
global Extended16_Label                  #main frame - extended TEDS
global Extended16_Entry                  #main frame - extended TEDS
global Extended17_Label                  #main frame - extended TEDS
global Extended17_Entry                  #main frame - extended TEDS
global Extended18_Label                  #main frame - extended TEDS
global Extended18_Entry                  #main frame - extended TEDS

global choice

global OnlineTEDSChoice                 # Global flag used to detect whether or not online TEDS were requested

#initialize choice
choice = "IEEE1451-4 Template 38 Thermistor"

OnlineTEDSChoice = False

#---------------------------------------SG_vTEDS GUI Based Function Definitions-----------------------------------------------
#MenuBar_File_Exit
def File_Exit():
    File_Close = tkMessageBox.askyesno(title = "Quit", message = "Are you sure you want to quit?")
    if File_Close == True:
        SG_vTEDS.destroy()
    return
#end GUI_Close

#MenuBar_File_New
#function clears the message boxes
def File_New():
    #clears entry boxes
    Basic_ManufacturerID_Entry.delete(0, END)
    Basic_ModelNumber_Entry.delete(0, END)
    Basic_VersionLetter_Entry.delete(0, END)
    Basic_VersionNumber_Entry.delete(0, END)
    Basic_SerialNumber_Entry.delete(0, END)

    #clears extended TEDS entry boxes
    Extended1_Entry.delete(0, END)
    Extended2_Entry.delete(0, END)
    Extended3_Entry.delete(0, END)
    Extended4_Entry.delete(0, END)
    Extended5_Entry.delete(0, END)
    Extended6_Entry.delete(0, END)
    Extended7_Entry.delete(0, END)
    Extended8_Entry.delete(0, END)
    Extended9_Entry.delete(0, END)
    Extended10_Entry.delete(0, END)
    Extended11_Entry.delete(0, END)
    Extended12_Entry.delete(0, END)
    Extended13_Entry.delete(0, END)
    Extended14_Entry.delete(0, END)
    Extended15_Entry.delete(0, END)
    Extended16_Entry.delete(0, END)
    Extended17_Entry.delete(0, END)
        
    return
#end File_New

#MenuBar_References_IEEE 1451-4
def Reference_IEEE14514():
    ieee1451_4 = tkMessageBox.showinfo(title = "IEEE 1451-4", message = "Use the following url for more information on IEEE 1451-4: https://standards.ieee.org/develop/regauth/tut/teds.pdf")
    return

#MenuBar_Help_What are TEDS?
def Help_WhatAreTEDS():
    WhatTEDS = tkMessageBox.showinfo(title = "What are vTEDS?", message = "Virtual Transducer Electronic Datasheets (vTEDS) are a binary files configured in a way defined by IEEE1451-4.  Each section of the binary word corresponds to a different datasheet value that is essential for your transducer.  Using this program, you can view and edit vTEDS!")
    return
#end Help_WhatAreTEDS

#MenuBar_Help_How do I read vTEDS?
def Help_HowDOIReadTEDS():
    HowRead = tkMessageBox.showinfo(title = "How do I read vTEDS?", message = "Using this program you can read a virtual transducer electronic datasheet (vTEDS) by clicking the 'Browse vTEDS Library' button.  This button will prompt you to load a file from the database.  Simply open the file and your TEDS will be displayed!")
    return
#end Help_HowDOIREADTEDS

#MenuBar_Help_How do I write vTEDS?
def Help_HowDOIWriteTEDS():
    HowWrite = tkMessageBox.showinfo(title = "How do I write vTEDS?", message = "Using this program you can write a virtual transducer electronic datasheet (vTEDS) by clicking the 'Save vTEDS As...' button.  This button will prompt you to browse to the vTEDS database, you then must choose a file name for your vTEDS and save.  This will write your custom vTEDS!")
    return


# When the user want xml from a website, we need to change our Global flag to True and then run our main Read_TEDS function
def OnlineTEDSRequest():
    global OnlineTEDSChoice
    OnlineTEDSChoice = True
    Read_TEDS()
    return


# This function reads in the xml file and converts it to text.
# To make this function useable for both local and remote xml files, we
# pass into this function an xml tree which is developed by the Read_TEDS function.
def ConvertFromXML(xmltree):
    root = xmltree.getroot()
    ID = root.find('ManufacturerID').text
    Mod = root.find('ModelNumber').text
    VLet = root.find('VersionLetter').text
    VNum = root.find('VersionNumber').text
    Ser = root.find('SerialNumber').text

    print(root.attrib['extended'])


    #We check to see if the Attribute "Extended" is true. If so, then we include the extended TEDS fields.
    if root.attrib['extended'] in ["true"]:
        print("Extended TEDS Detected")
        TID = root.find('TemplateID').text
        # From the template ID, we can easily figure out how to parse the xml file correctly by
        # using the templates laid out by 1451
        if TID in ["38"]:
            print("Template 38 found")
            MinT = root.find('MinTemp').text
            MaxT = root.find('MaxTemp').text
            MinR = root.find('MinResistance').text
            MaxR = root.find('MaxResistance').text
            ZeroC = root.find('Resistance0C').text
            CoA = root.find('CoefficientA').text
            CoB = root.find('CoefficientB').text
            CoC = root.find('CoefficientC').text
            SRT = root.find('ResponseTime').text
            NCE = root.find('Current').text
            MCE = root.find('MaxCurrent').text
            SHC = root.find('SelfHeat').text
            CalD = root.find('CalDate').text
            Cali = root.find('CalInit').text
            CalP = root.find('CalPer').text
            LID = root.find('LocationID').text
            return {'ID':ID, 'Mod':Mod, 'VLet':VLet, 'VNum':VNum, 'Ser':Ser, 'TID':TID, 'MinT':MinT, 'MaxT':MaxT, 'MinR':MinR, 'MaxR': MaxR, 'ZeroC':ZeroC, 'CoA':CoA, 'CoB':CoB, 'CoC':CoC, 'SRT':SRT,'NCE':NCE,'MCE':MCE,'SHC':SHC, 'CalD':CalD,'Cali':Cali,'CalP':CalP,'LID':LID}

    # If the template is not extended, then we just return the basic TEDS
    return {'ID':ID, 'Mod':Mod, 'VLet':VLet, 'VNum':VNum, 'Ser':Ser}
    

# This replaces pretty print in other xml libraries by adding whitespace and newlines.
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i




# This function wrties the current contents of the entry boxes to a vTEDS
def Write_TEDS():

    fileName = SaveAs_Entry.get()
    root = ET.Element("TEDs")
    
    # Might want to make this a function or subroutine
    ID_element = ET.SubElement(root, "ManufacturerID")
    Mod_element = ET.SubElement(root, "ModelNumber")
    VLet_element = ET.SubElement(root, "VersionLetter")
    VNum_element = ET.SubElement(root, "VersionNumber")
    Ser_element = ET.SubElement(root, "SerialNumber")
    

    # After initializing elements, set their text equal to what is in boxes
    ID_element.text = Basic_ManufacturerID_Entry.get()
    Mod_element.text = Basic_ModelNumber_Entry.get()
    VLet_element.text = Basic_VersionLetter_Entry.get()
    VNum_element.text = Basic_VersionNumber_Entry.get()
    Ser_element.text = Basic_SerialNumber_Entry.get()


    # If we have an extended TEDS Template chosen, we need to be able to save all of those elements.
    # This might need to be handled by another function which can handle the templates or somehow uses
    # a .xsd
    if choice.get() == "IEEE1451-4 Template 38 Thermistor":
        # We need to flag the XML file with the extended attribute
        root.set('extended', 'true')
        TID = ET.SubElement(root, "TemplateID")
        MinT = ET.SubElement(root, "MinTemp")
        MaxT = ET.SubElement(root, "MaxTemp")
        MinR = ET.SubElement(root, "MinResistance")
        MaxR = ET.SubElement(root, "MaxResistance")
        ZeroC = ET.SubElement(root, "Resistance0C")
        CoA = ET.SubElement(root, "CoefficientA")
        CoB = ET.SubElement(root, "CoefficientB")
        CoC = ET.SubElement(root, "CoefficientC")
        SRT = ET.SubElement(root, "ResponseTime")
        NCE = ET.SubElement(root, "Current")
        MCE = ET.SubElement(root, "MaxCurrent")
        SHC = ET.SubElement(root, "SelfHeat")
        CalD = ET.SubElement(root, "CalDate")
        Cali = ET.SubElement(root, "CalInit")
        CalP = ET.SubElement(root, "CalPer")
        LID = ET.SubElement(root, "LocationID")

        TID.text = Extended1_Entry.get()
        MinT.text = Extended2_Entry.get()
        MaxT.text = Extended3_Entry.get()
        MinR.text = Extended4_Entry.get()
        MaxR.text = Extended5_Entry.get()
        ZeroC.text = Extended6_Entry.get()
        CoA.text = Extended7_Entry.get()
        CoB.text = Extended8_Entry.get()
        CoC.text = Extended9_Entry.get()
        SRT.text = Extended10_Entry.get()
        NCE.text = Extended11_Entry.get()
        MCE.text = Extended12_Entry.get()
        SHC.text = Extended13_Entry.get()
        CalD.text = Extended14_Entry.get()
        Cali.text = Extended15_Entry.get()
        CalP.text = Extended16_Entry.get()
        LID.text = Extended17_Entry.get()

    else:
        # If there are no extended TEDS, we set the extended attribute to false
        root.set('extended', 'false')

    
    # Now we write out local changes to a file
    # We will make this an option on the GUI
    savePath = 'C://Users//Russty32280//GIT//IEEE-P21451-1//VirtualTEDS//vTEDS_Database'
    Complete_vTEDS_FileName = os.path.join(savePath, fileName)
    indent(root)
    tree = ET.ElementTree(root)
    tree.write(Complete_vTEDS_FileName)
    
#end of Write_Teds




#Read_TEDS is called either directly by pressing the Browse Button
# or through the Online Request. The global flag for Online TEDS will
# determine whether we need to pull the xml remotely or locally and
# then calls upon ConvertFromXML.
def Read_TEDS():
    global OnlineTEDSChoice
    if OnlineTEDSChoice:
        file = urllib2.urlopen(RequestTEDS_Entry.get())
        tree = ET.parse(file)
        file.close()
        OnlineTEDSChoice = False
    else:
        fileName = askopenfilename(parent=SG_vTEDS)
        tree = ET.parse(fileName)

    readTEDs = ConvertFromXML(tree)

    #clears entry boxes (basic)
    Basic_ManufacturerID_Entry.delete(0, END)
    Basic_ModelNumber_Entry.delete(0, END)
    Basic_VersionLetter_Entry.delete(0, END)
    Basic_VersionNumber_Entry.delete(0, END)
    Basic_SerialNumber_Entry.delete(0, END)

    
    #clears entry boxes (extended)
    Extended1_Entry.delete(0, END)
    Extended2_Entry.delete(0, END)
    Extended3_Entry.delete(0, END)
    Extended4_Entry.delete(0, END)
    Extended5_Entry.delete(0, END)
    Extended6_Entry.delete(0, END)
    Extended7_Entry.delete(0, END)
    Extended8_Entry.delete(0, END)
    Extended9_Entry.delete(0, END)
    Extended10_Entry.delete(0, END)
    Extended11_Entry.delete(0, END)
    Extended12_Entry.delete(0, END)
    Extended13_Entry.delete(0, END)
    Extended14_Entry.delete(0, END)
    Extended15_Entry.delete(0, END)
    Extended16_Entry.delete(0, END)
    Extended17_Entry.delete(0, END)
    


    #repopulates entry boxes (basic)
    Basic_ManufacturerID_Entry.insert(0, readTEDs['ID'])
    Basic_ModelNumber_Entry.insert(0, readTEDs['Mod'])
    Basic_VersionLetter_Entry.insert(0, readTEDs['VLet'])
    Basic_VersionNumber_Entry.insert(0, readTEDs['VNum'])
    Basic_SerialNumber_Entry.insert(0, readTEDs['Ser'])

    
    #repopulates entry boxes (extended)
    Extended1_Entry.insert(0, readTEDs['TID'])
    Extended2_Entry.insert(0, readTEDs['MinT'])
    Extended3_Entry.insert(0, readTEDs['MaxT'])
    Extended4_Entry.insert(0, readTEDs['MinR'])
    Extended5_Entry.insert(0, readTEDs['MaxR'])
    Extended6_Entry.insert(0, readTEDs['ZeroC'])
    Extended7_Entry.insert(0, readTEDs['CoA'])
    Extended8_Entry.insert(0, readTEDs['CoB'])
    Extended9_Entry.insert(0, readTEDs['CoC'])
    Extended10_Entry.insert(0, readTEDs['SRT'])
    Extended11_Entry.insert(0, readTEDs['NCE'])
    Extended12_Entry.insert(0, readTEDs['MCE'])
    Extended13_Entry.insert(0, readTEDs['SHC'])
    Extended14_Entry.insert(0, readTEDs['CalD'])
    Extended15_Entry.insert(0, readTEDs['Cali'])
    Extended16_Entry.insert(0, readTEDs['CalP'])
    Extended17_Entry.insert(0, readTEDs['LID'])
    
    return
#end Read_TEDS

def showExtendedTemplate(choice):
        
    if choice == "IEEE1451-4 Template 38 Thermistor":
        #extended TEDS Labels
        #T38 creates Template ID Label
        Extended1_Label.configure(text = "Template ID:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended1_Label.place(x = 415, y = 110)

        #T38 creates Minimum Temperature Label
        Extended2_Label.configure(text = "Min. Temp:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended2_Label.place(x = 415, y = 150)

        #T38 creates Maximum Temperature Label
        Extended3_Label.configure(text = "Max. Temp:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended3_Label.place(x = 415, y = 190)

        #T38 creates Minimum Resistance Label
        Extended4_Label.configure(text = "Min. Resistance:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended4_Label.place(x = 415, y = 230)

        #T38 creates Maximum Resistance Label
        Extended5_Label.configure(text = "Max. Resistance:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended5_Label.place(x = 415, y = 270)

        #T38 creates Resistance at 0C Label
        Extended6_Label.configure(text = "Resistance 0C:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended6_Label.place(x = 415, y = 310)

        #T38 creates Steinhart-Hart A Label
        Extended7_Label.configure(text = "Coefficient A:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended7_Label.place(x= 415, y = 350)

        #T38 creates Steinhart-Hart B Label
        Extended8_Label.configure(text = "Coefficient B:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended8_Label.place(x= 415, y = 390)

        #T38 creates Steinhart-Hart C Label
        Extended9_Label.configure(text = "Coefficient C:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended9_Label.place(x= 415, y = 430)

        #T38 creates Response Time Label
        Extended10_Label.configure(text = "Response Time:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended10_Label.place(x= 415, y = 470)

        #T38 creates Nominal Current Excitation Label
        Extended11_Label.configure(text = "Current:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended11_Label.place(x= 765, y = 110)

        #T38 creates Maximum Current Excitation Label
        Extended12_Label.configure(text = "Max Cur:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended12_Label.place(x= 765, y = 150)

        #T38 creates Self Heating Constant Label
        Extended13_Label.configure(text = "Self Heat:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended13_Label.place(x= 765, y = 190)

        #T38 creates Calibration Date Label
        Extended14_Label.configure(text = "Cal Date:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended14_Label.place(x= 765, y = 230)

        #T38 creates Calibration Initials Label
        Extended15_Label.configure(text = "Cal Init:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended15_Label.place(x= 765, y = 270)

        #T38 creates Calibration Period Label
        Extended16_Label.configure(text = "Cal Per:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended16_Label.place(x= 765, y = 310)

        #T38 creates Location Label
        Extended17_Label.configure(text = "Location:", font = ("Georgia",12), bg = "black", fg = "white")
        Extended17_Label.place(x= 765, y = 350) 

        #extended TEDS entry boxes
        #creates T38 Template ID entry box 
        Extended1_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended1_Entry.insert(0,"(Template ID)")
        Extended1_Entry.place(x = 545, y = 112)

        #creates T38 Minimum Temperature entry box
        Extended2_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended2_Entry.insert(0,"(Minimum Temperature)")
        Extended2_Entry.place(x = 545, y = 152)

        #creates T38 Maximum Temperature entry box
        Extended3_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended3_Entry.insert(0,"(Maximum Temperature)")
        Extended3_Entry.place(x = 545, y = 192)

        #creates T38 Minimum Resitance entry box
        Extended4_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended4_Entry.insert(0,"(Minimum Resistance)")
        Extended4_Entry.place(x = 545, y = 232)

        #creates T38 Maximum Resitance entry box
        Extended5_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended5_Entry.insert(0,"(Maximum Resistance)")
        Extended5_Entry.place(x = 545, y = 272)

        #creates T38 Resitance  0C entry box
        Extended6_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended6_Entry.insert(0,"(Resistance at 0C)")
        Extended6_Entry.place(x = 545, y = 312)

        #creates T38 Steinhart-Hart Coefficient A entry box
        Extended7_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended7_Entry.insert(0,"(Steinhart-Hart Coefficient)")
        Extended7_Entry.place(x = 545, y = 352)

        #creates T38 Steinhart-Hart Coefficient B entry box
        Extended8_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended8_Entry.insert(0,"(Steinhart-Hart Coefficient)")
        Extended8_Entry.place(x = 545, y = 392)

        #creates T38 Steinhart-Hart Coefficient C entry box
        Extended9_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended9_Entry.insert(0,"(Steinhart-Hart Coefficient)")
        Extended9_Entry.place(x = 545, y = 432)

        #creates T38 Response Time entry box
        Extended10_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended10_Entry.insert(0,"(Response Time)")
        Extended10_Entry.place(x = 545, y = 472)

        #creates T38 Nominal Current Excitation entry box 
        Extended11_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended11_Entry.insert(0,"(Nominal Current Excitation)")
        Extended11_Entry.place(x = 840, y = 112)

        #creates T38 Maximum Current Excitation entry box 
        Extended12_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended12_Entry.insert(0,"(Maximum Current Excitation)")
        Extended12_Entry.place(x = 840, y = 152)

        #creates T38 Self Heating Constant entry box 
        Extended13_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended13_Entry.insert(0,"(Self Heating Constant)")
        Extended13_Entry.place(x = 840, y = 192)

        #creates T38 Maximum Current Excitation entry box 
        Extended14_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended14_Entry.insert(0,"(Calibration Date)")
        Extended14_Entry.place(x = 840, y = 232)

        #creates T38 Maximum Current Excitation entry box 
        Extended15_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended15_Entry.insert(0,"(Calibration Initials)")
        Extended15_Entry.place(x = 840, y = 272)

        #creates T38 Maximum Current Excitation entry box 
        Extended16_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended16_Entry.insert(0,"(Calibration Period)")
        Extended16_Entry.place(x = 840, y = 312)

        #creates T38 Maximum Current Excitation entry box 
        Extended17_Entry.configure(font = ("Georgia",12), bg = "black", fg = "white")
        Extended17_Entry.insert(0,"(Location ID)")
        Extended17_Entry.place(x = 840, y = 352)

        
    return
#end showExtendedTemplate


#----------------------------------SG_vTEDS GUI Based Global Variable Initializations----------------------------------
#creates the GUI main frame/properties
SG_vTEDS = Tk()
SG_vTEDS.geometry("1080x540")
SG_vTEDS.title("CSD vTEDS Reader/Writer")
#creates background image display for main frame
SG_vTEDS_BG = PhotoImage(file ="C:\Users\Russty32280\Desktop\VirtualTEDS_GUIBG.gif")
SG_vTEDS_BGL = Label(image = SG_vTEDS_BG)
SG_vTEDS.image = SG_vTEDS_BG #keeps reference
SG_vTEDS_BGL.pack()
#NOTE: place background .gif file on computer and change the file path in photo image


#creates menu bar
SGvTEDSMenu = Menu(SG_vTEDS)

#Creates File Tab (menu bar)
SGvTEDSMenu_File = Menu(SGvTEDSMenu, tearoff = 0)
SGvTEDSMenu_File.add_command(label = "New", command = File_New)
SGvTEDSMenu_File.add_command(label = "Exit", command = File_Exit)

#Creates Reference Tab (menu bar)
SGvTEDSMenu_Reference = Menu(SGvTEDSMenu, tearoff = 0)
SGvTEDSMenu_Reference.add_command(label = "IEEE 1451-4", command = Reference_IEEE14514)
SGvTEDSMenu_Reference.add_command(label = "View TEDS Template Library")
SGvTEDSMenu_Reference.add_command(label = "Working Group")

#Creates Help Tab (menu bar)
SGvTEDSMenu_Help = Menu(SGvTEDSMenu, tearoff = 0)
SGvTEDSMenu_Help.add_command(label = "What are vTEDS?", command = Help_WhatAreTEDS)
SGvTEDSMenu_Help.add_command(label = "How do I read vTEDS?", command = Help_HowDOIReadTEDS)
SGvTEDSMenu_Help.add_command(label = "How do I write vTEDS?", command = Help_HowDOIWriteTEDS)

#configures the menu bar on the SG_vTEDS GUI
SGvTEDSMenu.add_cascade(label = "File", menu = SGvTEDSMenu_File)
SGvTEDSMenu.add_cascade(label = "Reference", menu = SGvTEDSMenu_Reference)
SGvTEDSMenu.add_cascade(label = "Help", menu = SGvTEDSMenu_Help)
SG_vTEDS.configure(menu = SGvTEDSMenu)


#creates SG_vTEDS title Label
SGvTEDS_TitleLabel = Label(SG_vTEDS, text = "SG-F2014 Virtual TEDS Reader/Writer", bg = "black", fg = "white")
SGvTEDS_TitleLabel.configure(font = ("Georgia",20))
SGvTEDS_TitleLabel.place(x=310,y=5)

#creates Basic TEDS Template Title Label
SGvTEDS_BasicTEDSLabel = Label(SG_vTEDS,  text = "IEEE 1451-4 Basic TEDS Template", bg = "black", fg = "white")
SGvTEDS_BasicTEDSLabel.configure(font = ("Georgia", 12))
SGvTEDS_BasicTEDSLabel.place(x=75, y = 60)

#creates Extended TEDS Template Title Label
SGvTEDS_ExtendedTEDSLabel = Label(SG_vTEDS, text = "Extended TEDS Template: ", bg = "black", fg = "white")
SGvTEDS_ExtendedTEDSLabel.configure(font = ("Georgia",12))
SGvTEDS_ExtendedTEDSLabel.place(x = 475, y = 60)

#Basic TEDS Labels
#creates basic TEDS manufacturer ID label
Basic_ManufacturerID_Label = Label(SG_vTEDS, text = "Manufacturer ID: ", bg = "black", fg = "white")
Basic_ManufacturerID_Label.configure(font = ("Georgia",12))
Basic_ManufacturerID_Label.place(x = 35, y = 110)

#creates basic TEDS Model Number Label
Basic_ModelNumber_Label = Label(SG_vTEDS, text = "Model Number: ", bg = "black", fg = "white")
Basic_ModelNumber_Label.configure(font = ("Georgia",12))
Basic_ModelNumber_Label.place(x = 35, y = 150)

#creates basic TEDS Version Letter Label
Basic_VersionLetter_Label = Label(SG_vTEDS, text = "Version Letter: ", bg = "black", fg = "white")
Basic_VersionLetter_Label.configure(font = ("Georgia",12))
Basic_VersionLetter_Label.place(x = 35, y = 190)

#creates basic TEDS Version Number Label
Basic_VersionNumber_Label = Label(SG_vTEDS, text = "Version Number: ", bg = "black", fg = "white")
Basic_VersionNumber_Label.configure(font = ("Georgia",12))
Basic_VersionNumber_Label.place(x = 35, y = 230)

#creates basic TEDS Serial Number Label
Basic_SerialNumber_Label = Label(SG_vTEDS, text = "Serial Number: ", bg = "black", fg = "white")
Basic_SerialNumber_Label.configure(font = ("Georgia",12))
Basic_SerialNumber_Label.place(x = 35, y = 270)

#Basic TEDS entry boxes
#creates basic TEDS manufacturer ID text entry box
Basic_ManufacturerID_Entry = Entry(bg = "black", fg ="white")
Basic_ManufacturerID_Entry.configure(font = ("Georgia",12))
Basic_ManufacturerID_Entry.insert(0, "(Manufacturer ID)")
Basic_ManufacturerID_Entry.place(x= 175, y = 112)

#creates basic TEDS Model Number text entry box
Basic_ModelNumber_Entry = Entry(bg = "black", fg ="white")
Basic_ModelNumber_Entry.configure(font = ("Georgia",12))
Basic_ModelNumber_Entry.insert(0, "(Model Number)")
Basic_ModelNumber_Entry.place(x= 175, y = 152)

#creates basic TEDS Version Letter text entry box
Basic_VersionLetter_Entry = Entry(bg = "black", fg ="white")
Basic_VersionLetter_Entry.configure(font = ("Georgia",12))
Basic_VersionLetter_Entry.insert(0, "(Version Letter)")
Basic_VersionLetter_Entry.place(x= 175, y = 192)

#creates basic TEDS Version Number text entry box
Basic_VersionNumber_Entry = Entry(bg = "black", fg ="white")
Basic_VersionNumber_Entry.configure(font = ("Georgia",12))
Basic_VersionNumber_Entry.insert(0, "(Version Number)")
Basic_VersionNumber_Entry.place(x= 175, y = 232)

#creates basic TEDS Serial Number text entry box
Basic_SerialNumber_Entry = Entry(bg = "black", fg ="white")
Basic_SerialNumber_Entry.configure(font = ("Georgia",12))
Basic_SerialNumber_Entry.insert(0, "(Serial Number)")
Basic_SerialNumber_Entry.place(x= 175, y = 272)

#TEDS Action Buttons
BrowseTEDSLibrary_Button = Button(SG_vTEDS, text = "Browse vTEDS Library", command = Read_TEDS, bg = "black", fg = "white")
BrowseTEDSLibrary_Button.configure(font = ("Georgia",12))
BrowseTEDSLibrary_Button.place(x = 130, y = 385)

SaveVTEDSAs_Button = Button(SG_vTEDS, text = "Save vTEDS As...", command = Write_TEDS, bg = "black", fg = "white")
SaveVTEDSAs_Button.configure(font = ("Georgia",12))
SaveVTEDSAs_Button.place(x = 35, y = 435)
#saveAs entry box
SaveAs_Entry = Entry(bg = "black", fg ="white")
SaveAs_Entry.configure(font = ("Georgia", 12))
SaveAs_Entry.insert(0,"(vTEDS File Name.txt)")
SaveAs_Entry.place(x=175, y = 439)


RequestTEDS_Button = Button(SG_vTEDS, text = "Request TEDS from", command = OnlineTEDSRequest, bg = "black", fg = "white")
RequestTEDS_Button.configure(font = ("Georgia",12))
RequestTEDS_Button.place(x = 25, y = 485)

RequestTEDS_Entry = Entry(bg = "black", fg ="white")
RequestTEDS_Entry.configure(font = ("Georgia", 12))
RequestTEDS_Entry.insert(0,"Full URL")
RequestTEDS_Entry.place(x=175, y = 485)





#extended TEDS
#extended TEDS option menu
#Defines possible choices in drop down menu and variable names
ExtendedTEDS_Options = ["IEEE1451-4 Template 36 Thermocouple","IEEE1451-4 Template 38 Thermistor"]
var = StringVar(SG_vTEDS)
var.set("No Extended TEDS Template Selected")
choice = var

#creates the drop down menu
ExtendedTemplate_Option = OptionMenu(SG_vTEDS, var, *ExtendedTEDS_Options, command = showExtendedTemplate)
ExtendedTemplate_Option.configure(font = ("Georgia",12))
ExtendedTemplate_Option.configure(bg = "black")
ExtendedTemplate_Option.configure(fg = "white")
ExtendedTemplate_Option.place(x = 675, y = 56)

#creates Extended TEDS Labels
Extended1_Label = Label(SG_vTEDS)
Extended2_Label = Label(SG_vTEDS)
Extended3_Label = Label(SG_vTEDS)
Extended4_Label = Label(SG_vTEDS)
Extended5_Label = Label(SG_vTEDS)
Extended6_Label = Label(SG_vTEDS)
Extended7_Label = Label(SG_vTEDS)
Extended8_Label = Label(SG_vTEDS)
Extended9_Label = Label(SG_vTEDS)
Extended10_Label = Label(SG_vTEDS)
Extended11_Label = Label(SG_vTEDS)
Extended12_Label = Label(SG_vTEDS)
Extended13_Label = Label(SG_vTEDS)
Extended14_Label = Label(SG_vTEDS)
Extended15_Label = Label(SG_vTEDS)
Extended16_Label = Label(SG_vTEDS)
Extended17_Label = Label(SG_vTEDS)
Extended18_Label = Label(SG_vTEDS)

#creates Extended TEDS entry boxes
Extended1_Entry = Entry(SG_vTEDS)
Extended2_Entry = Entry(SG_vTEDS)
Extended3_Entry = Entry(SG_vTEDS)
Extended4_Entry = Entry(SG_vTEDS)
Extended5_Entry = Entry(SG_vTEDS)
Extended6_Entry = Entry(SG_vTEDS)
Extended7_Entry = Entry(SG_vTEDS)
Extended8_Entry = Entry(SG_vTEDS)
Extended9_Entry = Entry(SG_vTEDS)
Extended10_Entry = Entry(SG_vTEDS)
Extended11_Entry = Entry(SG_vTEDS)
Extended12_Entry = Entry(SG_vTEDS)
Extended13_Entry = Entry(SG_vTEDS)
Extended14_Entry = Entry(SG_vTEDS)
Extended15_Entry = Entry(SG_vTEDS)
Extended16_Entry = Entry(SG_vTEDS)
Extended17_Entry = Entry(SG_vTEDS)
Extended18_Entry = Entry(SG_vTEDS)



#---------------------------------------------------SG_vTEDS Main Loop-----------------------------------------------------
#runs main loop
SG_vTEDS.mainloop()
