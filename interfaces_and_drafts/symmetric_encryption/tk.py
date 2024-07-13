import tkinter as tk
from tkinter import messagebox
from encrypt_decrypt import encrypt_data, decrypt_data
import binascii

def encrypt():
    password = password_entry.get()
    data = data_entry.get().encode('utf-8')
    encrypted_data = encrypt_data(password, data)
    encrypted_data_hex = binascii.hexlify(encrypted_data).decode()
    encrypted_data_entry.delete(0, tk.END)
    encrypted_data_entry.insert(0, encrypted_data_hex)

def decrypt():
    password = password_entry.get()
    encrypted_data_hex = encrypted_data_entry.get()
    encrypted_data = binascii.unhexlify(encrypted_data_hex)
    try:
        decrypted_data = decrypt_data(password, encrypted_data)
        messagebox.showinfo("Decrypted Data", decrypted_data.decode())
    except Exception as e:
        messagebox.showerror("Error", "Invalid password or encrypted data")


root = tk.Tk()
root.title("Encryption/Decryption")
root.configure(bg='black')

password_label = tk.Label(root, text="Password", fg='#90ee90', bg='black')
password_label.pack()
password_entry = tk.Entry(root, fg='#90ee90', bg='black')
password_entry.pack()

data_label = tk.Label(root, text="Data to encrypt", fg='#90ee90', bg='black')
data_label.pack()
data_entry = tk.Entry(root, fg='#90ee90', bg='black')
data_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, fg='#90ee90', bg='black')
encrypt_button.pack()

encrypted_data_label = tk.Label(root, text="Encrypted data", fg='#90ee90', bg='black')
encrypted_data_label.pack()
encrypted_data_entry = tk.Entry(root, fg='#90ee90', bg='black')
encrypted_data_entry.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, fg='#90ee90', bg='black')
decrypt_button.pack()

def close_app(event=None):
    root.destroy()

root.bind('<Return>', encrypt)
root.bind('<Control-w>', close_app)
root.bind('<Return>', encrypt)

root.mainloop()
