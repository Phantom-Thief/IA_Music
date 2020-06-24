#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jun 23, 2020 02:45:21 PM CEST  platform: Windows NT

import sys
import shutil
import os
from tkinter import filedialog
from main import *
import threading

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    root = tk.Tk()
    top = IMA(root)
    root.mainloop()

w = None
def create_IMA(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_IMA(root, *args, **kwargs)' .'''
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = IMA(w)
    return (w, top)

def destroy_IMA():
    global w
    w.destroy()
    w = None

class IMA:
    def __init__(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.a_thread = threading.Thread(target=self.run)
        self.a_selection = None
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 7"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x400+592+230")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("I.M.A")
        top.configure(background="#d9d9d9")

        self.ButtonRun = tk.Button(top)
        self.ButtonRun.place(relx=0.25, rely=0.3, height=63, width=300)
        self.ButtonRun.configure(activebackground="#b0b6e1")
        self.ButtonRun.configure(activeforeground="#000000")
        self.ButtonRun.configure(background="#d9d9d9")
        self.ButtonRun.configure(disabledforeground="#a3a3a3")
        self.ButtonRun.configure(foreground="#000000")
        self.ButtonRun.configure(command=self.run)
        self.ButtonRun.configure(highlightbackground="#d9d9d9")
        self.ButtonRun.configure(highlightcolor="black")
        self.ButtonRun.configure(pady="0")
        self.ButtonRun.configure(text='Play')

        self.ButtonStop = tk.Button(top)
        self.ButtonStop.place(relx=0.25, rely=0.3, height=63, width=300)
        self.ButtonStop.configure(activebackground="#b0b6e1")
        self.ButtonStop.configure(activeforeground="#000000")
        self.ButtonStop.configure(background="#d9d9d9")
        self.ButtonStop.configure(command=self.stop)
        self.ButtonStop.configure(disabledforeground="#a3a3a3")
        self.ButtonStop.configure(foreground="#000000")
        self.ButtonStop.configure(highlightbackground="#d9d9d9")
        self.ButtonStop.configure(highlightcolor="black")
        self.ButtonStop.configure(pady="0")
        self.ButtonStop.configure(text='Stop')
        self.ButtonStop.place_forget()

        self.ButtonSetting = tk.Button(top)
        self.ButtonSetting.place(relx=0.29, rely=0.5, height=63, width=250)
        self.ButtonSetting.configure(activebackground="#b0b6e1")
        self.ButtonSetting.configure(activeforeground="#000000")
        self.ButtonSetting.configure(background="#d9d9d9")
        self.ButtonSetting.configure(command=self.settingConfiguration)
        self.ButtonSetting.configure(disabledforeground="#a3a3a3")
        self.ButtonSetting.configure(foreground="#000000")
        self.ButtonSetting.configure(highlightbackground="#d9d9d9")
        self.ButtonSetting.configure(highlightcolor="black")
        self.ButtonSetting.configure(pady="0")
        self.ButtonSetting.configure(text='Setting')

        self.ButtonBackSetting = tk.Button(top)
        self.ButtonBackSetting.place(relx=0.75, rely=0.8, height=63, width=125)
        self.ButtonBackSetting.configure(activebackground="#b0b6e1")
        self.ButtonBackSetting.configure(activeforeground="#000000")
        self.ButtonBackSetting.configure(background="#d9d9d9")
        self.ButtonBackSetting.configure(command=self.exitSetting)
        self.ButtonBackSetting.configure(disabledforeground="#a3a3a3")
        self.ButtonBackSetting.configure(foreground="#000000")
        self.ButtonBackSetting.configure(highlightbackground="#d9d9d9")
        self.ButtonBackSetting.configure(highlightcolor="black")
        self.ButtonBackSetting.configure(pady="0")
        self.ButtonBackSetting.configure(text='back')
        self.ButtonBackSetting.place_forget()

        self.LabelTitle = tk.Label(top)
        self.LabelTitle.place(relx=0.417, rely=0.05, height=48, width=92)
        self.LabelTitle.configure(activebackground="#f0f0f0f0f0f0")
        self.LabelTitle.configure(background="#d9d9d9")
        self.LabelTitle.configure(disabledforeground="#a3a3a3")
        self.LabelTitle.configure(foreground="#000000")
        self.LabelTitle.configure(text='I.M.A')

        self.LabelSubTitle = tk.Label(top)
        self.LabelSubTitle.place(relx=0.25, rely=0.125, height=26, width=292)
        self.LabelSubTitle.configure(background="#d9d9d9")
        self.LabelSubTitle.configure(disabledforeground="#a3a3a3")
        self.LabelSubTitle.configure(font=font9)
        self.LabelSubTitle.configure(foreground="#000000")
        self.LabelSubTitle.configure(text='Adapt your Music to your GamePlay')

        self.ButtonMusic = tk.Button(top)
        self.ButtonMusic.place(relx=0.467, rely=0.28, height=33, width=48)
        self.ButtonMusic.configure(activebackground="#ececec")
        self.ButtonMusic.configure(command=self.putInFile)
        self.ButtonMusic.configure(activeforeground="#000000")
        self.ButtonMusic.configure(background="#d9d9d9")
        self.ButtonMusic.configure(cursor="fleur")
        self.ButtonMusic.configure(disabledforeground="#a3a3a3")
        self.ButtonMusic.configure(foreground="#000000")
        self.ButtonMusic.configure(highlightbackground="#d9d9d9")
        self.ButtonMusic.configure(highlightcolor="black")
        self.ButtonMusic.configure(pady="0")
        self.ButtonMusic.configure(text='Import')
        self.ButtonMusic.place_forget()

        self.LabelMusic = tk.Label(top)
        self.LabelMusic.place(relx=0.033, rely=0.30, height=26, width=132)
        self.LabelMusic.configure(background="#d9d9d9")
        self.LabelMusic.configure(disabledforeground="#a3a3a3")
        self.LabelMusic.configure(foreground="#000000")
        self.LabelMusic.configure(text='Add your music in :')
        self.LabelMusic.place_forget()

        self.ListboxMusic = tk.Listbox(top)
        self.ListboxMusic.place(relx=0.267, rely=0.255, relheight=0.14
                , relwidth=0.173)
        self.ListboxMusic.insert(1,"Calm")
        self.ListboxMusic.insert(2,"Action")
        self.ListboxMusic.insert(3,"Sad")
        self.ListboxMusic.bind('<<ListboxSelect>>', self.select)
        self.ListboxMusic.configure(background="white")
        self.ListboxMusic.configure(disabledforeground="#a3a3a3")
        self.ListboxMusic.configure(font="TkFixedFont")
        self.ListboxMusic.configure(foreground="#000000")
        self.ListboxMusic.configure(selectmode='single')
        self.ListboxMusic.place_forget()

        self.ButtonReset = tk.Button(top)
        self.ButtonReset.place(relx=0.033, rely=0.45, height=33, width=86)
        self.ButtonReset.configure(activebackground="#ececec")
        self.ButtonReset.configure(activeforeground="#000000")
        self.ButtonReset.configure(background="#d9d9d9")
        self.ButtonReset.configure(command=self.resetNorma)
        self.ButtonReset.configure(disabledforeground="#a3a3a3")
        self.ButtonReset.configure(foreground="#000000")
        self.ButtonReset.configure(highlightbackground="#d9d9d9")
        self.ButtonReset.configure(highlightcolor="black")
        self.ButtonReset.configure(pady="0")
        self.ButtonReset.configure(text='Recalibrate')
        self.ButtonReset.place_forget()

    def select(self,event):
        self.a_selection = self.ListboxMusic.selection_get()
    
    def putInFile(self):
        MusicFile = filedialog.askopenfilename(multiple=True ,filetypes=(("Wav file", "*.wav"),))
        
        try:
            shutil.copy2(MusicFile,"./musicologie/musiques/"+self.a_selection+"/")
            messagebox.showinfo("Done","The music is now in "+ str(self.a_selection))
        except:
            try:
                for i in MusicFile:
                    shutil.copy2(i,"./musicologie/musiques/"+self.a_selection+"/")
                messagebox.showinfo("Done","musics are now in "+ str(self.a_selection))
            except:
                messagebox.showerror("error", "Can't import") 

    def resetNorma(self):
        try :
            os.remove('normalize.dat')
            messagebox.showinfo("Done","The file is now recalibrate")
        except:
            messagebox.showerror("error", "This file is already recalibrate")

    def run(self):
        self.ButtonRun.configure(state=tk.DISABLED)
        self.hide(0)
        #main()
        self.ButtonStop.place(relx=0.25, rely=0.3, height=63, width=300)
        self.ButtonStop.configure(state=tk.ACTIVE)
        self.ButtonStop.update_idletasks()


    def stop(self):
        self.ButtonStop.configure(state=tk.DISABLED)
        self.ButtonStop.place_forget()
        #stopAll()
        self.show(0)
        self.ButtonRun.configure(state=tk.ACTIVE)
        self.ButtonRun.update_idletasks()

    def settingConfiguration(self):
        self.hide(0)
        self.show(1)
       
    def exitSetting(self):
        self.hide(1)
        self.show(0)
        
    def show(self, what):
        if what == 1:
            self.ButtonReset.place(relx=0.033, rely=0.45, height=33, width=86)
            self.ListboxMusic.place(relx=0.267, rely=0.255, relheight=0.14, relwidth=0.173)
            self.LabelMusic.place(relx=0.033, rely=0.30, height=26, width=132)
            self.ButtonMusic.place(relx=0.467, rely=0.28, height=33, width=48)
            self.ButtonBackSetting.place(relx=0.75, rely=0.8, height=63, width=125)
        else:
            self.ButtonRun.place(relx=0.25, rely=0.3, height=63, width=300)
            self.ButtonSetting.place(relx=0.29, rely=0.5, height=63, width=250)

    def hide(self, what):
        if what == 1:
            self.ButtonReset.place_forget()
            self.ListboxMusic.place_forget()
            self.LabelMusic.place_forget()
            self.ButtonMusic.place_forget()
            self.ButtonBackSetting.place_forget()
        else:
            self.ButtonRun.place_forget()
            self.ButtonSetting.place_forget()

if __name__ == '__main__':
    vp_start_gui()