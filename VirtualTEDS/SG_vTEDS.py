#Author: Tom Morris, Brian Finch
#Date: 10.30.2014
#Description: This code is a GUI for a vTEDS reader/writer. (IEEE1451-4)

#------------------------------------------------------Import Libraries--------------------------------------------------------
import sys
import os.path
from Tkinter import *
from tkFileDialog import *
import tkMessageBox


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

#initialize choice
choice = "IEEE1451-4 Template 38 Thermistor"


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

#This function reads a binary vTEDS text file and converts it to a readable format 
def ConvertFromBinary():
    #brings in file
    #text_file = open(str+".txt", "r")
    fileName = askopenfilename(parent=SG_vTEDS)
    text_file = open(fileName)
    f = text_file.readlines()
    text_file.close()

    x=f[0]

    #Basic TEDS
    #ID converted from binary
    ID=int(x[0:14], 2)
    #Model converted from binary
    Mod=int(x[14:29], 2)
    #Version Letter converted from binary into HEX
    VLet=int(x[29:34], 2)
    #Version Number converted from binary
    VNum=int(x[34:40], 2)
    #Serial converted from binary
    Ser=int(x[40:64], 2)

    #Extended TEDS Template 38
    TID = int(x[64:72], 2)
    MinT = int(x[72:83], 2)
    MaxT = int(x[83:94], 2)
    MinR = int(x[94:112], 2)
    MaxR = int(x[112:130], 2)
    ZeroC = int(x[130:150], 2)
    CoA = int(x[150:182], 2)
    CoB = int(x[182:214], 2)
    CoC = int(x[214:246], 2)
    SRT = int(x[246:252], 2)
    NCE = int(x[252:260], 2) 
    MCE = int(x[260:268], 2)
    SHC = int(x[268:273], 2)
    CalD = int(x[273:289], 2)
    Cali = int(x[289:304], 2)
    CalP = int(x[304:316], 2)
    LID = int(x[316:327], 2)

    return {'ID':ID, 'Mod':Mod, 'VLet':VLet, 'VNum':VNum, 'Ser':Ser, 'TID':TID, 'MinT':MinT, 'MaxT':MaxT, 'MinR':MinR, 'MaxR': MaxR, 'ZeroC':ZeroC, 'CoA':CoA, 'CoB':CoB, 'CoC':CoC, 'SRT':SRT,'NCE':NCE,'MCE':MCE,'SHC':SHC, 'CalD':CalD,'Cali':Cali,'CalP':CalP,'LID':LID}
#end ConvertFromBinary

#this function takes entered values from the text boxes and converts them to binary to write a vTEDS
def ConvertToBinary(integer, numBits):
    convertedBinaryString = bin(integer)[2:].zfill(numBits)
    
    return convertedBinaryString
#end ConvertToBinary

#this functions writes the currrent contents of the entry boxes to a vTEDS
def Write_TEDS():
    #receives text that is currently in the text entry boxes
    text_ManufacturerID = int(Basic_ManufacturerID_Entry.get())
    text_ModelNumber = int(Basic_ModelNumber_Entry.get())
    text_VersionLetter = int(Basic_VersionLetter_Entry.get())
    text_VersionNumber = int(Basic_VersionNumber_Entry.get())
    text_SerialNumber = int(Basic_SerialNumber_Entry.get())

    #converts text values to binary
    BasicTEDS0_14 = ConvertToBinary(text_ManufacturerID, 14)
    BasicTEDS14_29 = ConvertToBinary(text_ModelNumber, 15)
    BasicTEDS29_34 = ConvertToBinary(text_VersionLetter, 5)
    BasicTEDS34_40 = ConvertToBinary(text_VersionNumber, 6)
    BasicTEDS40_64 = ConvertToBinary(text_SerialNumber, 24)

    #writes extended TEDS option for IEEE Template 38

    text_381 = int(Extended1_Entry.get())
    text_382 = int(Extended2_Entry.get())
    text_383 = int(Extended3_Entry.get())
    text_384 = int(Extended4_Entry.get())
    text_385 = int(Extended5_Entry.get())
    text_386 = int(Extended6_Entry.get())
    text_387 = int(Extended7_Entry.get())
    text_388 = int(Extended8_Entry.get())
    text_389 = int(Extended9_Entry.get())
    text_3810 = int(Extended10_Entry.get())
    text_3811 = int(Extended11_Entry.get())
    text_3812 = int(Extended12_Entry.get())
    text_3813 = int(Extended13_Entry.get())
    text_3814 = int(Extended14_Entry.get())
    text_3815 = int(Extended15_Entry.get())
    text_3816 = int(Extended16_Entry.get())
    text_3817 = int(Extended17_Entry.get())
        

    ExtendedTEDS38_0_8 = ConvertToBinary(text_381, 8)
    ExtendedTEDS38_8_19 = ConvertToBinary(text_382, 11)
    ExtendedTEDS38_19_30 = ConvertToBinary(text_383, 11)
    ExtendedTEDS38_30_48 = ConvertToBinary(text_384, 18)
    ExtendedTEDS38_48_66 = ConvertToBinary(text_385, 18)
    ExtendedTEDS38_66_86 = ConvertToBinary(text_386, 20)
    ExtendedTEDS38_86_118 = ConvertToBinary(text_387, 32)
    ExtendedTEDS38_118_150 = ConvertToBinary(text_388, 32)
    ExtendedTEDS38_150_182 = ConvertToBinary(text_389, 32)
    ExtendedTEDS38_182_188 = ConvertToBinary(text_3810, 6)
    ExtendedTEDS38_188_196 = ConvertToBinary(text_3811, 8)
    ExtendedTEDS38_196_204 = ConvertToBinary(text_3812, 8)
    ExtendedTEDS38_204_209 = ConvertToBinary(text_3813, 5)
    ExtendedTEDS38_209_225 = ConvertToBinary(text_3814, 16)
    ExtendedTEDS38_225_240 = ConvertToBinary(text_3815, 15)
    ExtendedTEDS38_240_252 = ConvertToBinary(text_3816, 12)
    ExtendedTEDS38_252_263 = ConvertToBinary(text_3817, 11)
        

    #concatinates new vTED 
    Basic_vTEDS = BasicTEDS0_14 + BasicTEDS14_29 + BasicTEDS29_34 + BasicTEDS34_40 + BasicTEDS40_64
    Extended_vTEDS = ExtendedTEDS38_0_8 + ExtendedTEDS38_8_19 + ExtendedTEDS38_19_30 + ExtendedTEDS38_30_48 + ExtendedTEDS38_48_66 + ExtendedTEDS38_66_86 + ExtendedTEDS38_86_118 + ExtendedTEDS38_118_150 + ExtendedTEDS38_150_182 + ExtendedTEDS38_182_188 + ExtendedTEDS38_188_196 + ExtendedTEDS38_196_204 + ExtendedTEDS38_204_209  + ExtendedTEDS38_209_225+ ExtendedTEDS38_225_240 + ExtendedTEDS38_240_252 + ExtendedTEDS38_252_263     
    #saves new vTEDS

    #creates new file object with file path to the TEDS_database
    savePath = 'C://Users//Russty32280//Dropbox//vTEDS_Database//'
    fileName = SaveAs_Entry.get()
    Complete_vTEDS_FileName = os.path.join(savePath, fileName)
    New_vTEDS_File = open(Complete_vTEDS_FileName, 'w')

    #writes vTEDS to the new file of user input name
    New_vTEDS_File.write(Basic_vTEDS + Extended_vTEDS)
    New_vTEDS_File.close()

    return
#end Write_TEDS

#Browse vTEDS Library Button
def Read_TEDS():
    readTEDs = ConvertFromBinary()

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
SG_vTEDS.title("SG vTEDS Reader/Writer")
#creates background image display for main frame
SG_vTEDS_BG = PhotoImage(file = "C:\Users\Russty32280\Desktop\VirtualTEDS_GUIBG.gif")
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
