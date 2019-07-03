import requests
import bs4
from prettytable import PrettyTable
from tkinter import *
from tkinter import ttk

name = list()
code = list()
spo = list()

x = PrettyTable()
coder = list()
spojr = list()
total = list()


def call(q,p, u):
    #print(p,q,u)
    name.append(str(q))
    code.append(str(p))
    spo.append(str(u))
    codechef(str(p))
    spoj(str(u))
    x = PrettyTable(["name", "codechef handle", "spoj handle", "codechef questions", "spoj questions"])
    for i in range(0, len(name)):
        x.add_row([name[i], code[i], spo[i], coder[i], spojr[i]])
    print(x)
    print("-------------")



def codechef(user):
    p = "https://codechef.com/users/"
    r = user
    q = str(p) + str(r)
    res = requests.get(q)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    coder.append(len(soup.article.getText().split()) - 1)
    return;


def spoj(user):
    p = "https://spoj.com/users/"
    r = user
    q = p + r
    res = requests.get(q)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    spojr.append((int(soup.dd.getText())))

    return;


    #total.append(coder[i] + spojr[i])







root=Tk()
root.geometry("1380x768")
#root.resizable(0,0)

label_1=Label(root,text="username")
label_2=Label(root,text="codechef handle")
label_3=Label(root,text="spoj handle")
entry_1=Entry(root)
entry_2=Entry(root)
entry_3=Entry(root)
label_1.place(x=1150,y=300)
label_2.place(x=1150,y=345)
label_3.place(x=1150,y=390)
entry_1.place(x=1150,y=325)
entry_2.place(x=1150,y=370)
entry_3.place(x=1150,y=415)

button=Button(root,text="submit",fg="blue",activebackground="yellow",command=lambda:call(entry_1.get(),entry_2.get(),entry_3.get()))
button.place(x=1150,y=420)
canvas = Canvas(root, width= 1920, height= 680)
canvas.place()
imsge1=PhotoImage(file='C:\\Users\\Arnab\\Desktop\\attachments\\1.jpg')
canvas.create_image(0 , 0, anchor = NW , image=image1)
root.mainloop()
