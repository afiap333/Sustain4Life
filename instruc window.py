from tkinter import *

tk2 = Tk()
tk2.geometry("700x1000")
back = Frame(tk2,bg="#064789",width=700,height=1000)
back.place(x=0,y=0)
inst = Label(back, text="Instructions", font=("Franklin Gothic Demi Cond",45), fg="#A5BE00", bg="#064789")
inst.place(x=210,y=180)
desc = Label(back, text="At the beginning of each month, a new prompt will be\nreleased targeting a certain sustainability goal to attain.\nTake pictures of yourself completing the task and \nupload your images into the 'Input' page. Submissions will be \ncollected periodically and logged in so you can compare\n your performace with your friends and others.", font=("Franklin Gothic Demi Cond",20), fg="#ebf2fa", bg="#064789")
desc.place(x=25,y=300)
next3 = Button(back, text="Start/Continue Submission",  font=("Franklin Gothic Demi Cond",15), fg="#ebf2fa",bg="#679436")
next3.place(x=230,y=570)
tk2.mainloop()