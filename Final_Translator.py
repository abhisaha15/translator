from tkinter import *
from PIL import ImageTk, Image
from translate import Translator

root = Tk()

#width x height
root.geometry("650x450")
#root.minsize(650, 450)
#root.maxsize(650, 450)
root.resizable(False,False)
root.title("Translator")
root.iconbitmap("img/language-solid.ico")

my_pic= Image.open("img/logo_2.png")

#Resize Image
resized= my_pic.resize((650, 450), Image.ANTIALIAS)
new_pic= ImageTk.PhotoImage(resized)
#Image size 500x375 / 250
my_label=Label(root, image= new_pic)
my_label.pack(pady=0)
def buttoncopy():

    root.clipboard_clear()
    root.clipboard_append(OutputVar.get())

#for txt
photo_1 = PhotoImage(file = "img/paste-regular.png")
photoimage_1 = photo_1.subsample(15,15)
TextVar = StringVar()
#TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)

input_str =Entry(root,textvariable=TextVar,width=42,font=("Times New Roman","12"))
input_str.place(x=150,y=115)
#inp=StringVar(input_str)

b1 = Button(root, fg="red", image= photoimage_1, compound= LEFT, command= lambda:input_str.event_generate("<<Paste>>"),text=" Paste",font=("Times New Roman","12"))
b1.place(x=500,y=110)

LanguageChoices = {'Hindi','English','French','German','Spanish'}
#InputLanguageChoice.set('English')
#TranslateLanguageChoice.set('Hindi')
clicked = StringVar()
clicked.set("Select The Entry Language")
drop = OptionMenu(root, clicked, *LanguageChoices)
drop.place(x=130,y=165)
clicked1 = StringVar()
clicked1.set("Select The Desired Language")
drop1 = OptionMenu(root, clicked1, *LanguageChoices)
drop1.place(x=330,y=165)
def Translate():
    translator = Translator(from_lang= clicked.get(),to_lang=clicked1.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


b2 = Button(root, fg="red", text="Translate",command=Translate,font=("Times New Roman","24"))
b2.place(x=260,y=225)

OutputVar = StringVar()
output = Entry(root,textvariable=OutputVar,width=42,font=("Times New Roman","12"))
output.place(x=150,y=315)


photo_2 = PhotoImage(file = "img/copy-regular.png")
photoimage_2 = photo_2.subsample(15,15)

b3 = Button(root, fg="red", image= photoimage_2, compound= LEFT,command=buttoncopy,text=" Copy",font=("Times New Roman","12"))
b3.place(x=500,y=310)

root.mainloop()