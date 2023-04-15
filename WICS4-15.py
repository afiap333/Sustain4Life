from tkinter import *
#from PIL import Image, ImageTk
master = Tk()


master.geometry("700x1000")
frame = Frame(master, bg="#427AA1",width=700,height=1000)
frame.place(x=0, y=0)


createProfile = Label(master, text = "Create your profile!", font=("Franklin Gothic Demi Cond",45),fg="#A5BE00",bg="#427AA1")

firstName = Label(master, text = "Enter your first name", font=("Franklin Gothic Demi Cond",25),fg="#A5BE00",bg="#427AA1")
lastName = Label(master, text = "Enter your last name", font=("Franklin Gothic Demi Cond",25),fg="#A5BE00",bg="#427AA1")
userName = Label(master, text = "Enter you username:", font=("Franklin Gothic Demi Cond",25),fg="#A5BE00",bg="#427AA1")
overEighteen = Label(master, text = "Are you over 18?", font=("Franklin Gothic Demi Cond", 25),fg="#A5BE00",bg="#427AA1")

#column 0
createProfile.grid(row = 0, sticky = W, pady = 2)
firstName.grid(row = 1, column = 0, sticky = W, pady = 2)
lastName.grid(row = 2, column = 0, sticky = W, pady = 2)
userName.grid(row = 3, column = 0, sticky = W, pady = 2)
overEighteen.grid(row = 4, column = 0, sticky = W, pady = 2)

efirstName = Entry(master)
elastName = Entry(master)
euserName = Entry(master)
yesVar = IntVar()
Checkbutton(master, text = "Yes", variable = yesVar, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 5, column = 0, sticky = W, pady=2)
noVar = IntVar()
Checkbutton(master, text = "No", variable = noVar, fg="#A5BE00",bg="#427AA1", activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 6, column = 0, sticky = W, pady=2)

p1Var = IntVar()
Checkbutton(master, text = "Cat1", variable = p1Var, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 8, column = 0, pady=2)
p2Var = IntVar()
Checkbutton(master, text = "Cat2", variable = p2Var, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 8, column = 1, pady=2)
p3Var = IntVar()
Checkbutton(master, text = "Dinosaur", variable = p3Var, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 10, column = 0, pady=2)
p4Var = IntVar()
Checkbutton(master, text = "Koala bear", variable = p4Var, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 10, column = 1, pady=2)
p5Var = IntVar()
Checkbutton(master, text = "Rabbit", variable = p5Var, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 12, column = 0, pady=2)
p6Var = IntVar()
Checkbutton(master, text = "Penguin", variable = p6Var, fg="#A5BE00",bg="#427AA1",activebackground="#427AA1", activeforeground="#A5BE00",font=("Franklin Gothic Demi Cond",15)).grid(row = 12, column = 1, pady=2)


#column 1
efirstName.grid(row = 1, column = 1, pady = 2)
elastName.grid(row = 2, column =1, pady = 2)
euserName.grid(row = 3, column = 1, pady = 2)
"""

image1 = PhotoImage(file = "Cat1.png")
image1 = image1.subsample(4,4);
profile1 = Label(master, image = image1)
profile1.grid(row = 7, column = 0, pady =2)
profile1.image = image1


image2 = PhotoImage(file = "Cat21.png")
image2 = image2.subsample(2,2)
profile2 = Label(master, image = image2)
profile2.grid(row = 7, column = 1, pady =2)
profile2.image = image2


image3 = PhotoImage(file = "Dinosaur1..png")
image3 = image3.subsample(2,2)
profile3 = Label(master, image = image3)
profile3.grid(row = 9, column = 0, pady =2)
profile3.image = image3


image4 = PhotoImage(file = "koala1.png")
image4 = image4.subsample(2,2)
profile4 = Label(master, image = image4)
profile4.grid(row = 9, column = 1, pady =2)
profile4.image = image4


image5 = PhotoImage(file = "rabbit1.png")
image5 = image5.subsample(2,2);
profile5 = Label(master, image = image5)
profile5.grid(row = 11, column = 0, pady =2)
profile5.image = image5


image6 = PhotoImage(file = "penguin1.png")
image6 = image6.subsample(2,2)
profile6 = Label(master, image = image6)
profile6.grid(row = 11, column = 1, pady =2)
profile6.image = image6
"""



mainloop()

