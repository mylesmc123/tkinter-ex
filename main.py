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
lbl = Label(tkWindow, text="RAS Project File (*.prj)")
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=2,
                width=100)
inputtxt.pack()

# Label Creation
lbl = Label(tkWindow, text="RAS Boundary Shapefile File (*.shp)")
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=2,
                width=100)
inputtxt.pack()

button = Button(tkWindow,
                text='Extract RAS meta data.',
                command=showMsg)
button.pack()

# Separator object
separator = ttk.Separator(tkWindow, orient='horizontal')
# separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
separator.pack(fill='x')

# Label Creation
lbl = Label(tkWindow, text="HMS Project File (*.hms)")
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=2,
                width=100)
inputtxt.pack()

# Label Creation
lbl = Label(tkWindow, text="HMS Boundary Shapefile File (*.shp)")
lbl.pack()
# tkWindow.mainloop()

# TextBox Creation
inputtxt = Text(tkWindow,
                height=2,
                width=100)
inputtxt.pack()

button = Button(tkWindow,
                text='Extract HMS meta data.',
                command=showMsg)
button.pack()

tkWindow.mainloop()
