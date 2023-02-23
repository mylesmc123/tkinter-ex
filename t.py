from tkinter import *
from tkinter import ttk
from tkinter import filedialog
gui = Tk()
gui.geometry("400x400")
gui.title("FC")


class FileSelect(Frame):
    def __init__(self, parent=None, fileDescription="", **kw):
        Frame.__init__(self, master=parent, **kw)
        self.filePath = StringVar()
        self.lblName = Label(self, text=fileDescription)
        self.lblName.grid(row=0, column=0)
        self.entPath = Entry(self, textvariable=self.filePath)
        self.entPath.grid(row=0, column=1)
        self.btnFind = ttk.Button(
            self, text="Browse...", command=self.setFilePath)
        self.btnFind.grid(row=0, column=2)

    def setFilePath(self):
        file_selected = filedialog.askopenfilename(
            # filetypes=[("Excel files", ".xlsx .xls")]
            filetypes=[("File Types", ".dss .hms .prj .shp .geojson .json")])
        self.filePath.set(file_selected)

    @property
    def file_path(self):
        return self.filePath.get()


class FolderSelect(Frame):
    def __init__(self, parent=None, folderDescription="", **kw):
        Frame.__init__(self, master=parent, **kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0, column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0, column=1)
        self.btnFind = ttk.Button(
            self, text="Browse...", command=self.setFolderPath)
        self.btnFind.grid(row=0, column=2)

    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)

    @property
    def folder_path(self):
        return self.folderPath.get()


def doStuff():
    file1 = file1Select.file_path
    file2 = file2Select.file_path
    file3 = file3Select.file_path
    print("Doing stuff with file", file1, file2, file3)


filePath = StringVar()

file1Select = FileSelect(gui, "RAS project file (.prj)")
file1Select.grid(row=0)

file2Select = FileSelect(gui, "RAS boundary shape file (*.shp) ")
file2Select.grid(row=1)


c = ttk.Button(gui, text="Extract RAS MetaData", command=doStuff)
c.grid(row=4, column=0)

# Separator object
separator = ttk.Separator(gui, orient='horizontal')
separator.grid(row=5, ipady=10)

file1Select = FileSelect(gui, "HMS project file (.prj)")
file1Select.grid(row=6)

file2Select = FileSelect(gui, "HMS boundary shape file (*.shp) ")
file2Select.grid(row=7)

folder3Select = FolderSelect(gui, "Optional. DSS Data Directory.")
folder3Select.grid(row=8)

c2 = ttk.Button(gui, text="Extract HMS MetaData", command=doStuff)
c2.grid(row=9, column=0)

gui.mainloop()
