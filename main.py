import gui
import tkinter

def voteMenu():
    print(
        "-----------------------------\n" +
        "VOTE MENU\n" +
        "-----------------------------"
        )
    vote = input("v: Vote \nx: Exit \nOption: ").strip().lower()
    while vote != "x" and vote != "v":
        vote = input("Invalid (v/x): ").strip().lower()
    return vote

def candidateMenu():
    print(
    "-----------------------------\n" +
    "CANDIDATE MENU\n" +
    "-----------------------------"
    )
    vote = "Joe"
    choice = int(input("1: John \n2: Jane \nCandidate:\t").strip())
    while choice != 2 and choice != 1:
        choice = int(input("Invalid (1/2): ").strip())
    if choice == 1:
        vote = "John"
    else:
        vote = "Jane"
    print(f"Voted {vote}")
    return vote

def main():
    root = tkinter.Tk()
    root.title("Lab 10")
    root.geometry("240x220")
    root.resizable(width=False, height=False)

    gui.Gui(root)

    root.mainloop()
    


main()
