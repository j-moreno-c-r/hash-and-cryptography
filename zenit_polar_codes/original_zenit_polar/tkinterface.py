import tkinter as tk
from zenitpolar import encrypt

def encrypt_text():
    text = text_entry.get()
    encrypted_text = encrypt(text)
    output_label.config(text=encrypted_text)
def main_tk():
    global text_entry, output_label
    root = tk.Tk()
    root.configure(bg='black')

    title_label = tk.Label(root, text="Zenit\nPolar", fg="green", bg="black", font=("Helvetica", 16))
    title_label.pack()

    text_entry = tk.Entry(root, fg="green", bg="black")
    text_entry.pack()

    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text, fg="green", bg="black")
    encrypt_button.pack()

    output_label = tk.Label(root, text="", fg="green", bg="black")
    output_label.pack()
    
    root.bind('<Return>', lambda event: encrypt_text())
    root.bind('<Control-w>', lambda event: root.destroy())    
    root.mainloop()