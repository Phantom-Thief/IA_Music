import sys
import shutil
import os
from tkinter import filedialog
from main import *
import pickle

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
    root.iconbitmap('1.0.0/LogoIMA.ico')
    top = IMA(root)
    root.mainloop()
    top.stopcroix()
    

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


        try :
            self.VSV = pickle.load(open("volume.dat", 'rb'))
        except :
            self.VSV = 10

        self.a_selection = None
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9"
        font13 = "-family {Segoe UI} -size 13"
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
        top.resizable(width=False, height=False)
        top.title("I.M.A")
        top.configure(background="#606060")

        self.LabelTitle = tk.Label(top)
        self.LabelTitle.place(relx=0.4, rely=0.05, height=48, width=92)
        self.LabelTitle.configure(activebackground="#f0f0f0f0f0f0")
        self.LabelTitle.configure(background="#606060")
        self.LabelTitle.configure(font=font13)
        self.LabelTitle.configure(disabledforeground="#a3a3a3")
        self.LabelTitle.configure(foreground="#000000")
        self.LabelTitle.configure(text='I.M.A')

        self.LabelSubTitle = tk.Label(top)
        self.LabelSubTitle.place(relx=0.24, rely=0.125, height=26, width=292)
        self.LabelSubTitle.configure(background="#606060")
        self.LabelSubTitle.configure(disabledforeground="#a3a3a3")
        self.LabelSubTitle.configure(font=font9)
        self.LabelSubTitle.configure(foreground="#000000")
        self.LabelSubTitle.configure(text='Adapt your Music to your GamePlay')

        self.ButtonRun = tk.Button(top)
        self.ButtonRun.place(relx=0.23, rely=0.3, height=63, width=300)
        self.ButtonRun.configure(activebackground="#b0b6e1")
        self.ButtonRun.configure(activeforeground="#000000")
        self.ButtonRun.configure(background="#808080")
        self.ButtonRun.configure(disabledforeground="#a3a3a3")
        self.ButtonRun.configure(foreground="#000000")
        self.ButtonRun.configure(command=self.run)
        self.ButtonRun.configure(highlightbackground="#d9d9d9")
        self.ButtonRun.configure(highlightcolor="black")
        self.ButtonRun.configure(pady="0")
        self.ButtonRun.configure(text='Play')

        self.ButtonStop = tk.Button(top)
        self.ButtonStop.configure(activebackground="#b0b6e1")
        self.ButtonStop.configure(activeforeground="#000000")
        self.ButtonStop.configure(background="#808080")
        self.ButtonStop.configure(command=self.stop)
        self.ButtonStop.configure(disabledforeground="#a3a3a3")
        self.ButtonStop.configure(foreground="#000000")
        self.ButtonStop.configure(highlightbackground="#606060")
        self.ButtonStop.configure(highlightcolor="black")
        self.ButtonStop.configure(pady="0")
        self.ButtonStop.configure(text='Stop')
        self.ButtonStop.place_forget()

        self.ButtonSetting = tk.Button(top)
        self.ButtonSetting.place(relx=0.27, rely=0.5, height=63, width=250)
        self.ButtonSetting.configure(activebackground="#b0b6e1")
        self.ButtonSetting.configure(activeforeground="#000000")
        self.ButtonSetting.configure(background="#808080")
        self.ButtonSetting.configure(command=lambda: self.settingConfiguration(0,1))
        self.ButtonSetting.configure(disabledforeground="#a3a3a3")
        self.ButtonSetting.configure(foreground="#000000")
        self.ButtonSetting.configure(highlightbackground="#606060")
        self.ButtonSetting.configure(highlightcolor="black")
        self.ButtonSetting.configure(pady="0")
        self.ButtonSetting.configure(text='Setting')

        self.ButtonCredit = tk.Button(top)
        self.ButtonCredit.place(relx=0.308, rely=0.7, height=63, width=200)
        self.ButtonCredit.configure(activebackground="#b0b6e1")
        self.ButtonCredit.configure(activeforeground="#000000")
        self.ButtonCredit.configure(background="#808080")
        self.ButtonCredit.configure(command=lambda: self.settingConfiguration(0,3))
        self.ButtonCredit.configure(disabledforeground="#a3a3a3")
        self.ButtonCredit.configure(foreground="#000000")
        self.ButtonCredit.configure(highlightbackground="#606060")
        self.ButtonCredit.configure(highlightcolor="black")
        self.ButtonCredit.configure(pady="0")
        self.ButtonCredit.configure(text='Credit')

        self.LabelCredit = tk.Text(top)
        self.LabelCredit.configure(background="#606060")
        self.LabelCredit.configure(font=font9)
        text="""This project was done by :

    Nicolas Brun, Thomas Menchi, Jérôme Kacimi, Alexis Chevalier and Théo Guerrois.

    On behalf of all this team we really thank you for downloading our application.
                                                
                                                
                                                Have fun and win your games."""
        self.LabelCredit.insert('1.0', text)
        self.LabelCredit.configure(state='disabled')
        
        self.ButtonBackSetting = tk.Button(top)
        self.ButtonBackSetting.configure(activebackground="#b0b6e1")
        self.ButtonBackSetting.configure(activeforeground="#000000")
        self.ButtonBackSetting.configure(background="#808080")
        self.ButtonBackSetting.configure(command=lambda: self.exitSetting(1,0))
        self.ButtonBackSetting.configure(disabledforeground="#a3a3a3")
        self.ButtonBackSetting.configure(foreground="#000000")
        self.ButtonBackSetting.configure(highlightbackground="#606060")
        self.ButtonBackSetting.configure(highlightcolor="black")
        self.ButtonBackSetting.configure(pady="0")
        self.ButtonBackSetting.configure(text='done')

        self.ButtonMusicSetting = tk.Button(top)
        self.ButtonMusicSetting.configure(activebackground="#b0b6e1")
        self.ButtonMusicSetting.configure(activeforeground="#000000")
        self.ButtonMusicSetting.configure(background="#808080")
        self.ButtonMusicSetting.configure(command=lambda: self.settingConfiguration(1,2))
        self.ButtonMusicSetting.configure(disabledforeground="#a3a3a3")
        self.ButtonMusicSetting.configure(foreground="#000000")
        self.ButtonMusicSetting.configure(highlightbackground="#606060")
        self.ButtonMusicSetting.configure(highlightcolor="black")
        self.ButtonMusicSetting.configure(pady="0")
        self.ButtonMusicSetting.configure(text='Music')

        self.ButtonMusicBackSetting = tk.Button(top)
        self.ButtonMusicBackSetting.configure(activebackground="#b0b6e1")
        self.ButtonMusicBackSetting.configure(activeforeground="#000000")
        self.ButtonMusicBackSetting.configure(background="#808080")
        self.ButtonMusicBackSetting.configure(command=lambda: self.exitSetting(2,1))
        self.ButtonMusicBackSetting.configure(disabledforeground="#a3a3a3")
        self.ButtonMusicBackSetting.configure(foreground="#000000")
        self.ButtonMusicBackSetting.configure(highlightbackground="#606060")
        self.ButtonMusicBackSetting.configure(highlightcolor="black")
        self.ButtonMusicBackSetting.configure(pady="0")
        self.ButtonMusicBackSetting.configure(text='done')

        self.ButtonMusic = tk.Button(top)
        self.ButtonMusic.configure(activebackground="#ececec")
        self.ButtonMusic.configure(command=self.putInFile)
        self.ButtonMusic.configure(activeforeground="#000000")
        self.ButtonMusic.configure(background="#808080")
        self.ButtonMusic.configure(disabledforeground="#a3a3a3")
        self.ButtonMusic.configure(foreground="#000000")
        self.ButtonMusic.configure(highlightbackground="#606060")
        self.ButtonMusic.configure(highlightcolor="black")
        self.ButtonMusic.configure(pady="0")
        self.ButtonMusic.configure(text='Import')

        self.LabelMusic = tk.Label(top)
        self.LabelMusic.configure(background="#606060")
        self.LabelMusic.configure(disabledforeground="#a3a3a3")
        self.LabelMusic.configure(foreground="#000000")
        self.LabelMusic.configure(text='Add your music in :')

        self.SetVolume = tk.Scale(top)
        self.SetVolume.configure(orient='horizontal')
        self.SetVolume.configure(background="#808080")
        self.SetVolume.configure(from_=0.0)
        self.SetVolume.configure(to=100.0)
        self.SetVolume.configure(resolution=1)
        self.SetVolume.set(self.VSV)
        self.SetVolume.configure(tickinterval=50)
        self.SetVolume.configure(command=self.defVolume)
        self.SetVolume.configure(label='Volume')

        self.ListboxMusic = tk.Listbox(top)
        self.ListboxMusic.insert(1,"Calm")
        self.ListboxMusic.insert(2,"Action")
        self.ListboxMusic.insert(3,"Sad")
        self.ListboxMusic.bind('<<ListboxSelect>>', self.select)
        self.ListboxMusic.configure(background="gray")
        self.ListboxMusic.configure(disabledforeground="#a3a3a3")
        self.ListboxMusic.configure(font="TkFixedFont")
        self.ListboxMusic.configure(foreground="#000000")
        self.ListboxMusic.configure(selectmode='single')

        self.ButtonReset = tk.Button(top)
        self.ButtonReset.configure(activebackground="#ececec")
        self.ButtonReset.configure(activeforeground="#000000")
        self.ButtonReset.configure(background="#808080")
        self.ButtonReset.configure(command=self.resetNorma)
        self.ButtonReset.configure(disabledforeground="#a3a3a3")
        self.ButtonReset.configure(foreground="#000000")
        self.ButtonReset.configure(highlightbackground="#606060")
        self.ButtonReset.configure(highlightcolor="black")
        self.ButtonReset.configure(pady="0")
        self.ButtonReset.configure(text='Recalibrate AI sensitivity')

    def select(self,event):
        self.a_selection = self.ListboxMusic.selection_get()
    

    def putInFile(self):
        MusicFile = filedialog.askopenfilename(multiple=True ,filetypes=(("Wav file", "*.wav"),("Mp3 file","*.mp3"),
                                                                        ("all file","*.*")))
        if MusicFile is not "":
            typefile = MusicFile[0].split('/')[-1].split('.')[-1]
            if typefile == 'wav':
                try:
                    shutil.copy2(MusicFile,"./musicologie/musiques/"+self.a_selection+"/")
                    messagebox.showinfo("Done","The music is now in "+ str(self.a_selection))
                except:
                    try:
                        for i in MusicFile:
                            shutil.copy2(i,"./musicologie/musiques/"+self.a_selection+"/")
                        messagebox.showinfo("Done","musics are now in "+ str(self.a_selection))
                    except:
                        messagebox.showerror("error", "Can't import in None") 
            else:
                messagebox.showerror("error", "pls convert this file to a .wav")

    def resetNorma(self):
        try :
            os.remove('normalize.dat')
            messagebox.showinfo("Done","The file is now recalibrate")
        except:
            messagebox.showerror("error", "This file is already recalibrate")


    def defVolume(self,p_vol):
        self.VSV = p_vol
         

    def run(self):
        self.hide(0)
        main(float(self.VSV)/100)
        stopHooker(True)
        self.ButtonStop.place(relx=0.23, rely=0.3, height=63, width=300)
        self.ButtonStop.update_idletasks()

    def stopcroix(self):
        stopHooker(False)
        pickle.dump(self.VSV, open("volume.dat", 'wb'))

    def stop(self):
        stopHooker(False)
        pickle.dump(self.VSV, open("volume.dat", 'wb'))
        self.ButtonStop.place_forget()
        self.show(0)

    def settingConfiguration(self, hide, show):
        self.hide(hide)
        self.show(show)
       
    def exitSetting(self, hide, show):
        self.hide(hide)
        self.show(show)

    def show(self, p_what):
        if p_what == 0:
            self.ButtonRun.place(relx=0.23, rely=0.3, height=63, width=300)
            self.ButtonSetting.place(relx=0.27, rely=0.5, height=63, width=250)
            self.ButtonCredit.place(relx=0.308, rely=0.7, height=63, width=200)
            
        if p_what == 1:            
            self.ButtonReset.place(relx=0.35, rely=0.52, height=63, width=140)
            self.ButtonBackSetting.place(relx=0.8, rely=0.8, height=63, width=100)
            self.ButtonMusicSetting.place(relx=0.35, rely=0.3, height=63, width=140)
        
        if p_what == 2:
            self.ListboxMusic.place(relx=0.41, rely=0.355, relheight=0.14, relwidth=0.173)
            self.LabelMusic.place(relx=0.2, rely=0.40, height=26, width=132)
            self.ButtonMusic.place(relx=0.6, rely=0.38, height=33, width=48)
            self.SetVolume.place(relx=0.23, rely=0.55, height=75, width=300)
            self.ButtonMusicBackSetting.place(relx=0.8, rely=0.8, height=63, width=100)
        
        if p_what == 3:
            self.LabelCredit.place(relx=0.1, rely=0.3, height=150, width=475)
            self.ButtonBackSetting.place(relx=0.8, rely=0.8, height=63, width=100)

    def hide(self, p_what):
        if p_what == 0:
            self.ButtonRun.place_forget()
            self.ButtonSetting.place_forget()
            self.ButtonCredit.place_forget()

        if p_what == 1:
            self.ButtonReset.place_forget()
            self.ButtonBackSetting.place_forget()
            self.ButtonMusicSetting.place_forget()
            self.LabelCredit.place_forget()

        if p_what == 2:
            self.ListboxMusic.place_forget()
            self.LabelMusic.place_forget()
            self.ButtonMusic.place_forget()
            self.SetVolume.place_forget()
            self.ButtonMusicBackSetting.place_forget()


if __name__ == '__main__':
    vp_start_gui()