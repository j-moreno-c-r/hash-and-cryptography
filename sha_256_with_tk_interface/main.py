import tkinter as tk
from sha_encrypter import encrypter

def encrypt_input(event=None):
    result = encrypter(phrase_entry.get())
    result_label['text'] = result

def close_window(event=None):
    root.destroy()

root = tk.Tk()
root.configure(bg='black')

phrase_entry = tk.Entry(root, width=50, fg='#32CD32', bg='black')
phrase_entry.pack(pady=20)
phrase_entry.bind('<Return>', encrypt_input)
phrase_entry.focus_set()  

encrypt_button = tk.Button(root, text="Generate the sha 256 hash", command=encrypt_input, fg='#32CD32', bg='black')
encrypt_button.pack(pady=20)

result_label = tk.Label(root, text="", fg='#32CD32', bg='black')
result_label.pack(pady=20)

root.bind('<Control-w>', close_window)

if __name__ == "__main__":
    root.mainloop()