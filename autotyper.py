import pyautogui
import keyboard
import time
import tkinter as tk
from tkinter.filedialog import askopenfile


pointer_position = [0, 0]


def main():
    root = tk.Tk()
    root.title('AutoTyper')
    root.configure(bg='#2f3136')
    root.resizable(width=False, height=False)

    # Instruction for detection
    inst_detect = tk.Label(root, text='Click the button below')
    inst_detect.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_detect.grid(row=1, column=3)
    inst_detect2 = tk.Label(root, text='Put the mouse pointer to where you want to autotype')
    inst_detect2.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_detect2.grid(row=2, column=3)
    inst_detect3 = tk.Label(root, text='Press "Ctrl"')
    inst_detect3.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_detect3.grid(row=3, column=3)

    def detect_pointer():
        keyboard.wait('ctrl')
        pointer_position[0] = pyautogui.position()[0]
        pointer_position[1] = pyautogui.position()[1]

        if pointer_position[0] and pointer_position[1]:
            click_txt.set(f'Position detected: {pointer_position[0]}, {pointer_position[1]}')
        
    # Left click on where the user wants to type in
    click_txt = tk.StringVar()
    click_btn = tk.Button(root, command=detect_pointer, textvariable=click_txt, height=1, width=25)
    click_btn.config(font=('Arial', 15), fg='#b9bbbe', bg='#3a4c48')
    click_btn.grid(row=4, column=3, pady=15)
    click_txt.set('Detect')

    # Instruction for browsing
    inst_browse = tk.Label(root, text='Choose a txt file to autotype with line by line')
    inst_browse.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_browse.grid(row=5, column=3)
    inst_browse2 = tk.Label(root, text='Choose typing interval (seconds)')
    inst_browse2.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_browse2.grid(row=6, column=3)
    inst_browse3 = tk.Label(root, text='The process will start as soon as you choose a file')
    inst_browse3.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_browse3.grid(row=7, column=3)
    inst_browse4 = tk.Label(root, text='Hold "esc" to exit the program')
    inst_browse4.config(font=('Helvetica', 15), fg='#b9bbbe', bg='#2f3136')
    inst_browse4.grid(row=8, column=3)
    
    def autotype_file():
        browse_txt.set('loading...')
        infile = askopenfile(parent=root, mode='rb', title='Choose a file')
        
        if infile:
            pyautogui.click(pointer_position[0], pointer_position[1])
            time.sleep(1)
            for line in infile:
                browse_txt.set('typing...')

                if keyboard.is_pressed("esc"):
                    browse_txt.set('Browse')
                    break
                
                pyautogui.write(format_str(line))
                pyautogui.press('enter')
                time.sleep(int(interval_entry.get()))

            stop_autotyping()
            print('Autotyping stopped.')
        browse_txt.set('Browse')

    # Time interval between typing
    drop_txt = tk.StringVar()
    drop_txt.set('2')
    interval_entry = tk.ttk.Entry(root, textvariable=drop_txt)
    
    drop = tk.OptionMenu(root, drop_txt, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')
    drop.config(font=('Arial', 15), fg='#b9bbbe', bg='#3a4c48')
    drop.grid(row=9, column=3, pady=10)

    # Browse button
    browse_txt = tk.StringVar()
    browse_btn = tk.Button(root, command=autotype_file, textvariable=browse_txt, height=1, width=7)
    browse_btn.config(font=('Arial', 15), fg='#b9bbbe', bg='#3a4c48')
    browse_txt.set('Browse')
    browse_btn.grid(row=10, column=3, pady=10)

    root.mainloop()

def format_str(my_str):
    my_str = str(my_str)
    my_str = my_str[2 : len(my_str)-5 : ]
    return(my_str)

def stop_autotyping():
    tk.messagebox.showinfo('AutoTyper', 'Autotyping stopped.')


main()