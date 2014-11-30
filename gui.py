from Tkinter import *
from ttk import *
import tkFileDialog
import os


filename = ""
ifLabel1 = None
ifLabel2 = None
ifLabel3 = None
ifLabel4 = None
ofLabel1 = None
ofLabel2 = None
ofLabel3 = None


def tabOneCommand(text1, text2, text3):
    if text1 != "" or text2 != "" or text3 != "":
        cmdstring = "python exploit-withoutsaving.py %s %s %s" % (text1, text2, text3)
        os.system(cmdstring)

def tabTwoCommand(text1, text2, text3, text4):
    if text1 != "" or text2 != "" or text3 != "" or text4 != "":
        cmdstring = "python exploit.py %s %s %s %s" % (text1, text2, text3, text4)
        os.system(cmdstring)

def tabThreeCommand(text1, text2, text3):
    if text1 != "" or text2 != "" or text3 != "":
        cmdstring = "python grab.py %s %s %s" % (text1, text2, text3)
        os.system(cmdstring)

def tabFourCommand(text1, text2):
    if text1 != "" or text2 != "":
        cmdstring = "python split.py %s %s" % (text1, text2)
        os.system(cmdstring)

def tabFiveCommand(text1, text2, text3):
    if text1 != "" or text2 != "" or text3 != "":
        cmdstring1 = "python single_aux.py %s" % (text1)
        os.system(cmdstring1)
        cmdstring2 = "python exploit.py temp_spear.txt 1000000 %s %s" % (text2, text3)
        print "working..."
        os.system(cmdstring2)
        print "working..."


def getFile(button):
    global filename
    filename = tkFileDialog.askopenfilename(filetypes=[])
    if button == 1:
        global ifLabel1
        ifLabel1['text'] = filename
    elif button == 2:
        global ifLabel2
        ifLabel2['text'] = filename
    elif button == 3:
        global ofLabel1
        ofLabel1['text'] = filename
    elif button == 4:
        global ifLabel3
        ifLabel3['text'] = filename
    elif button == 5:
        global ofLabel2
        ofLabel2['text'] = filename
    elif button == 6:
        global ifLabel4
        ifLabel4['text'] = filename
    elif button == 7:
        global ofLabel3
        ofLabel3['text'] = filename

def removeFile(button):
    if button == 1:
        global ifLabel1
        ifLabel1['text'] = "No file chosen"
    elif button == 2:
        global ifLabel2
        ifLabel2['text'] = "No file chosen"
    elif button == 3:
        global ofLabel1
        ofLabel1['text'] = "No file chosen"
    elif button == 4:
        global ifLabel3
        ifLabel3['text'] = "No file chosen"
    elif button == 5:
        global ofLabel2
        ofLabel2['text'] = "No file chosen"
    elif button == 6:
        global ifLabel4
        ifLabel4['text'] = "No file chosen"
    elif button == 7:
        global ofLabel3
        ofLabel3['text'] = "No file chosen"
    
    

#---------------------------------------
#
#             Main method
#
#---------------------------------------

def main():


    root = Tk()
    root.title("Heart Attack")
    #scheduledimage=PhotoImage(...)
    n = Notebook(root)

    tab1 = Frame(n)
    tab2 = Frame(n)
    tab3 = Frame(n)
    tab4 = Frame(n)
    tab5 = Frame(n)

    n.add(tab1, text = "Exploit Without Saving")
    n.add(tab2, text = "Exploit and Save")
    n.add(tab3, text = "Grab Sites")
    n.add(tab4, text = "Split Up Files")
    n.add(tab5, text = "Single Site")
    n.grid(row=0, column=0)

#Tab1

    # First entry that saves filename
    l1 = Label(tab1, text="Input File:")
    l1.grid(row=0, column=0)
    #l1.grid(row=0, column=0)
    ifButton1 = Button(tab1, text="Choose File", command=lambda:getFile(1))
    ifButton1.grid(row=0,column=2)
    rmButton1 = Button(tab1, text="Remove", command=lambda:removeFile(1))
    rmButton1.grid(row=0,column=3)
    #ifButton1.grid(row=0, column=0)
    global ifLabel1
    ifLabel1 = Label(tab1, text="No file chosen", foreground="RED")
    ifLabel1.grid(row=0,column=1)
    #ifLabel1.grid(row=0, column=0)

    #Second field for number of sites, default 1000000
    l2 = Label(tab1, text="Number of Sites:")
    l2.grid(row=1,column=0)
    #l2.grid(row=0, column=0)
    e2 = Entry(tab1)
    e2.grid(row=1,column=1)
    #e2.grid(row=0, column=0)
    e2.insert(0, "1000000")

    #Third field for number of iterations
    l3 = Label(tab1, text="Iterations:")
    l3.grid(row=2,column=0)
    #l3.grid(row=0, column=0)
    e3 = Entry(tab1)
    e3.grid(row=2,column=1)
    #e3.grid(row=0, column=0)
   
    #Button to run function
    b1 = Button(tab1, text="Go", command=lambda:tabOneCommand(ifLabel1['text'], e2.get(), e3.get()))
    b1.grid(row=3, column=1)

#Tab2

    # First entry that saves filename
    l4 = Label(tab2, text="Input File:")
    l4.grid(row=0, column=0)
    ifButton2 = Button(tab2, text="Choose File", command=lambda:getFile(2))
    ifButton2.grid(row=0, column=2)
    rmButton2 = Button(tab2, text="Remove", command=lambda:removeFile(2))
    rmButton2.grid(row=0,column=3)
    global ifLabel2
    ifLabel2 = Label(tab2, text="No file chosen", foreground="RED")
    ifLabel2.grid(row=0, column=1)

    #Second field for number of sites, default 1000000
    l5 = Label(tab2, text="Number of Sites:")
    l5.grid(row=1, column=0)
    e5 = Entry(tab2)
    e5.grid(row=1, column=1)
    e5.insert(0, "1000000")

    #Third field for number of iterations
    l6 = Label(tab2, text="Iterations:")
    l6.grid(row=2, column=0)
    e6 = Entry(tab2)
    e6.grid(row=2, column=1)

    #Fourth field for output file
    l7 = Label(tab2, text="Output File:")
    l7.grid(row=3, column=0)
    ofButton1 = Button(tab2, text="Choose File", command=lambda:getFile(3))
    ofButton1.grid(row=3, column=2)
    rmButton3 = Button(tab2, text="Remove", command=lambda:removeFile(3))
    rmButton3.grid(row=3,column=3)
    global ofLabel1
    ofLabel1 = Label(tab2, text="No file chosen", foreground="RED")
    ofLabel1.grid(row=3, column=1)
    
    #print(filename)
   
    #Button to run function
    b2 = Button(tab2, text="Go", command=lambda:tabTwoCommand(ifLabel2['text'], e5.get(),e6.get(), ofLabel1['text']))
    b2.grid(row=4, column=1)

#Tab3

    # First entry that saves filename
    l8 = Label(tab3, text="Input File:")
    l8.grid(row=0, column=0)
    ifButton3 = Button(tab3, text="Choose File", command=lambda:getFile(4))
    ifButton3.grid(row=0, column=2)
    rmButton4 = Button(tab3, text="Remove", command=lambda:removeFile(4))
    rmButton4.grid(row=0,column=3)
    global ifLabel3
    ifLabel3 = Label(tab3, text="No file chosen", foreground="RED")
    ifLabel3.grid(row=0, column=1)

    #Second field for number of sites, default 1000000
    l9 = Label(tab3, text="Sites:")
    l9.grid(row=1, column=0)
    e9 = Entry(tab3)
    e9.grid(row=1, column=1)
    e9.insert(0, "1000000")

    #Fourth field for output file
    l10 = Label(tab3, text="Output File:")
    l10.grid(row=2, column=0)
    ofButton2 = Button(tab3, text="Choose File", command=lambda:getFile(5))
    ofButton2.grid(row=2, column=2)
    rmButton5 = Button(tab3, text="Remove", command=lambda:removeFile(5))
    rmButton5.grid(row=2,column=3)
    global ofLabel2
    ofLabel2 = Label(tab3, text="No file chosen", foreground="RED")
    ofLabel2.grid(row=2, column=1)
    
    #print(filename)
   
    #Button to run function
    b3 = Button(tab3, text="Go", command=lambda:tabThreeCommand(ifLabel3['text'], e9.get(), ofLabel2['text']))
    b3.grid(row=3, column=1)

#Tab4

    # First entry that saves filename
    l11 = Label(tab4, text="Input File:")
    l11.grid(row=0, column=0)
    ifButton4 = Button(tab4, text="Choose File", command=lambda:getFile(6))
    ifButton4.grid(row=0, column=2)
    rmButton6 = Button(tab4, text="Remove", command=lambda:removeFile(6))
    rmButton6.grid(row=0,column=3)
    global ifLabel4
    ifLabel4 = Label(tab4, text="No file chosen", foreground="RED")
    ifLabel4.grid(row=0, column=1)


    #Second field for number of pieces
    l12 = Label(tab4, text="Pieces:")
    l12.grid(row=1, column=0)
    e12 = Entry(tab4)
    e12.grid(row=1, column=1)

    
    #print(filename)
   
    #Button to run function
    b4 = Button(tab4, text="Go", command=lambda:tabFourCommand(ifLabel4['text'], e12.get()))
    b4.grid(row=2, column=1)

#Tab5

    # First entry to input site
    l13 = Label(tab5, text="Input Site:")
    l13.grid(row=0, column=0)
    e13 = Entry(tab5)
    e13.grid(row=0, column=1)


    l15 = Label(tab5, text="Iterations:")
    l15.grid(row=1,column=0)
    #l3.grid(row=0, column=0)
    e15 = Entry(tab5)
    e15.grid(row=1,column=1)


    #Second field for output file
    l14 = Label(tab5, text="Output File:")
    l14.grid(row=2, column=0)
    ofButton3 = Button(tab5, text="Choose File", command=lambda:getFile(7))
    ofButton3.grid(row=2, column=2)
    rmButton7 = Button(tab5, text="Remove", command=lambda:removeFile(7))
    rmButton7.grid(row=2,column=3)
    global ofLabel3
    ofLabel3 = Label(tab5, text="No file chosen", foreground="RED")
    ofLabel3.grid(row=2, column=1)

    
    #print(filename)
   
    #Button to run function
    b5 = Button(tab5, text="Go", command=lambda:tabFiveCommand(e13.get(), e15.get(),ofLabel3['text']))
    b5.grid(row=3, column=1)


    root.mainloop()
    exit()


if __name__ == '__main__':
    main()  

