from tkinter import *
from tkinter import messagebox, ttk

tkWindow = Tk()
tkWindow.geometry('800x450')
tkWindow.title('Meta Data Extractor for HEC Models')


def showMsg():
    # messagebox.showinfo('Message', 'You clicked the Submit button!')
    for i in range(10):
        print(i)


# Label Creation
lbl = Label(tkWindow, text="RAS Project File (*.prj)", pady=10)
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=1,
                width=100,
                pady=1)
inputtxt.pack()

# Label Creation
lbl = Label(tkWindow, text="RAS Boundary Shapefile File (*.shp)", pady=10)
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=1,
                width=100,
                pady=1)
inputtxt.pack()

button = Button(tkWindow,
                text='Extract RAS meta data.',
                command=showMsg,
                pady=10)
button.pack(pady=10)

# Separator object
separator = ttk.Separator(tkWindow, orient='horizontal')
separator.pack(fill='x', pady=10)

# Label Creation
lbl = Label(tkWindow, text="HMS Project File (*.hms)", pady=10)
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=1,
                width=100,
                pady=1)
inputtxt.pack()

# Label Creation
lbl = Label(tkWindow, text="HMS Boundary Shapefile File (*.shp)", pady=10)
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=1,
                width=100,
                pady=1)
inputtxt.pack()

button = Button(tkWindow,
                text='Extract HMS meta data.',
                command=showMsg,
                pady=10)
button.pack(pady=10)

tkWindow.mainloop()
