import gui
import tkinter

def main():
    root = tkinter.Tk()
    root.title("Lab 1 Redux")
    root.geometry("240x220")
    root.resizable(width=False, height=False)

    gui.Gui(root)

    root.mainloop()
    


main()
