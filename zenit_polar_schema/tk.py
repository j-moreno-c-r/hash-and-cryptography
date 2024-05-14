import tkinter as tk
from encryption import encrypt_decrypt


def run_interface():
    def encrypt_decrypt_button_click(event=None):
        test_word = word_entry.get()
        encrypted_word, decrypted_word, zenit, polar = encrypt_decrypt(test_word)
        encrypted_word_label.config(text="Encrypted word: " + encrypted_word)
        decrypted_word_label.config(text="Decrypted word: " + decrypted_word)
        zenit_label.config(text="Zenit: " + zenit)
        polar_label.config(text="Polar: " + polar)

    def close_window(event):
        window.destroy()

    window = tk.Tk()
    window.configure(bg='black')
    window.bind('<Control-w>', close_window)
    window.bind('<Return>', encrypt_decrypt_button_click)

    word_label = tk.Label(window, text="Enter a word to encrypt and decrypt:", bg='black', fg='#00ff00')
    word_label.pack()

    word_entry = tk.Entry(window, bg='black', fg='#00ff00', insertbackground='#00ff00')
    word_entry.pack()

    encrypt_decrypt_button = tk.Button(window, text="Encrypt and Decrypt", command=encrypt_decrypt_button_click, bg='black', fg='#00ff00')
    encrypt_decrypt_button.pack()

    encrypted_word_label = tk.Label(window, text="", bg='black', fg='#00ff00')
    encrypted_word_label.pack()

    decrypted_word_label = tk.Label(window, text="", bg='black', fg='#00ff00')
    decrypted_word_label.pack()

    zenit_label = tk.Label(window, text="", bg='black', fg='#00ff00')
    zenit_label.pack()

    polar_label = tk.Label(window, text="", bg='black', fg='#00ff00')
    polar_label.pack()

    window.mainloop()