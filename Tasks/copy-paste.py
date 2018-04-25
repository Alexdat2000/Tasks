import tkinter
c = tkinter.Tk()
c.withdraw()
clip = c.clipboard_get()
c.update()
c.destroy()
print(clip)