import tkinter as tk
import textwrap
from encrypt_decrypt import encrypt, decrypt
from generate_keys import generate_keys


private_key, public_key = generate_keys()
    

def encrypt_message(event=None):
    message = message_entry.get()
    encrypted_message = encrypt(public_key, message.encode())
    formatted_encrypted_message = textwrap.fill(str(encrypted_message), 50)  # Quebra a mensagem em linhas de no máximo 50 caracteres
    encrypted_message_label.config(text="Encrypted: " + formatted_encrypted_message)

def decrypt_message(event=None):
    encrypted_message = encrypted_message_label.cget("text").replace("Encrypted: ", "").replace('\n', '')
    decrypted_message = decrypt(private_key, eval(encrypted_message))
    decrypted_message_label.config(text="Decrypted: " + decrypted_message.decode())

def toggle_private_key():
    if private_key_label.winfo_viewable():
        private_key_label.pack_forget()
    else:
        private_key_label.pack()

def toggle_public_key():
    if public_key_label.winfo_viewable():
        public_key_label.pack_forget()
    else:
        public_key_label.pack()

def close_program(event=None):
    root.destroy()

root = tk.Tk()
root.configure(bg='black')
def main():
    global root, message_entry, encrypted_message_label, decrypted_message_label,private_key_label, public_key_label, toggle_button_public_key, toggle_button_private_key, encrypt_button, decrypt_button

    private_key, public_key = generate_keys()

    private_key_label = tk.Label(root, text="Private Key: " + '\n'.join(textwrap.wrap(str(private_key), 50)), fg='#90EE90', bg='black')
    public_key_label = tk.Label(root, text="Public Key: " + '\n'.join(textwrap.wrap(str(public_key), 50)), fg='#90EE90', bg='black')

    toggle_button_public_key = tk.Button(root, text="Public Key", command=toggle_public_key, fg='#90EE90', bg='black')
    toggle_button_public_key.pack()

    toggle_button_private_key = tk.Button(root, text="Private Key", command=toggle_private_key, fg='#90EE90', bg='black')
    toggle_button_private_key.pack()

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


    root.bind('<Control-w>', close_program)

    root.mainloop()


