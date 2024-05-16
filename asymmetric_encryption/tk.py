import tkinter as tk
import textwrap
from generate_keys import generate_keys
from encrypt_decrypt import encrypt, decrypt

def encrypt_message(event=None):
    message = message_entry.get()
    encrypted_message = encrypt(public_key, message.encode())
    encrypted_message_label.config(text="Encrypted: " + str(encrypted_message))

def decrypt_message(event=None):
    encrypted_message = encrypted_message_label.cget("text").replace("Encrypted: ", "")
    decrypted_message = decrypt(private_key, eval(encrypted_message))
    decrypted_message_label.config(text="Decrypted: " + decrypted_message.decode())

def close_program(event=None):
    root.destroy()

root = tk.Tk()
root.configure(bg='black')

private_key, public_key = generate_keys()

private_key_label = tk.Label(root, text="Private Key: " + '\n'.join(textwrap.wrap(str(private_key), 50)), fg='#90EE90', bg='black')
private_key_label.pack()

public_key_label = tk.Label(root, text="Public Key: " + '\n'.join(textwrap.wrap(str(public_key), 50)), fg='#90EE90', bg='black')
public_key_label.pack()

message_label = tk.Label(root, text="Enter a message:", fg='#90EE90', bg='black')
message_label.pack()

message_entry = tk.Entry(root, fg='#90EE90', bg='black')
message_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, fg='#90EE90', bg='black')
encrypt_button.pack()

encrypted_message_label = tk.Label(root, text="", fg='#90EE90', bg='black')
encrypted_message_label.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, fg='#90EE90', bg='black')
decrypt_button.pack()

decrypted_message_label = tk.Label(root, text="", fg='#90EE90', bg='black')
decrypted_message_label.pack()

root.bind('<Return>', encrypt_message)
root.bind('<Control-w>', close_program)

root.mainloop()