from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES



def change(text='type',src='English',dest='Hindi'):
    text1 = text
    src1 = src
    dest1 = dest

    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt_box.get(1.0,END)
    textget = change(text=msg,src=s,dest=d)
    dest_txt_box.delete(1.0,END)
    dest_txt_box.insert(END,textget)

root = Tk()
root.title("Our Translator")
root.geometry("500x600")
root.config(bg='Red')

lab_txt = Label(root,text="Translator", font=("Arial",30,"bold"))
lab_txt.place(x=100,y=40,height=40,width=300)

frame = Frame(root).pack(side=BOTTOM)

sor_txt = Label(root,text="Source Text", font=("Arial",18,"bold"),bg='Red',fg='white')
sor_txt.place(x=100,y=120,height=20,width=300)

 
sor_txt_box = Text(frame, font=("Arial",20,"bold"),wrap=WORD)
sor_txt_box.place(x=40, y=150, height=100, width=400)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=40, y=270, height=20, width=140)
comb_sor.set('English')

button_change = Button(frame,text="Translate", relief=RAISED, bg='yellow',command=data)
button_change.place(x=200, y=270, height=20, width=60)

comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=270, y=270, height=20, width=140)
comb_dest.set('English')



dest_txt = Label(root,text="Destination Text", font=("Arial",18,"bold"),bg='Red',fg='white')
dest_txt.place(x=100,y=320,height=20,width=300)

dest_txt_box = Text(frame, font=("Arial",20,"bold"),wrap=WORD)
dest_txt_box.place(x=40, y=350, height=100, width=400)



root.mainloop()