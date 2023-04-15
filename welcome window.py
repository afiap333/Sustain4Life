from tkinter import *

tk = Tk()
tk.geometry("700x1000")
frame = Frame(tk,bg="#679436",width=700,height=1000)
frame.place(x=0,y=0)
title = Label(frame, text="Welcome\nto\nSustain4Life!", font=("Franklin Gothic Demi Cond",70),fg="#ebf2fa",bg="#679436")
title.place(x=350,y=350,anchor="center")

next = Button(frame, text="Start Here", command=tk.destroy,font=("Franklin Gothic Demi Cond",20),fg="#679436",bg="#ebf2fa")
next.place(x=280,y=600)
tk.mainloop()



