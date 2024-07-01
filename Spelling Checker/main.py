import tkinter
from tkinter import*
from textblob import TextBlob

root =Tk()
root.title("SPELLING CHECKER")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word=enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root,text="Correct word is :",font=("poppins",21),bg="#dae6f6",fg="white")
    cs.place(x=100,y=250)
    spell.config(text=right) 

heading = Label(root,text="Spellling Checker",font=("trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

enter_text = Entry(root,justify="center",width="32",font=("Times of New Roman",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="violet",command=check_spelling)
button.pack()

spell = Label(root,font=("poppins",20), bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)

root.mainloop()