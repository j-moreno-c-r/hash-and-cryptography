import random
import string
import tkinter as tk
from tkinter import messagebox

def decrypt(data, zenit, polar):
    decrypt_dict = {p: z for z, p in zip(zenit, polar)}
    decrypt_dict = {p: z for z, p in zip(zenit, polar)} 
    return ''.join(decrypt_dict.get(c, c) for c in data)

def encrypt(data, zenit, polar):
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    encrypt_dict = {z: p for z, p in zip(zenit, polar)}
    return ''.join(encrypt_dict.get(c, c) for c in data)

def generate_two_unique_words(length):
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    word1 = ''.join(letters[:length])
    word2 = ''.join(letters[length:length*2])
    return word1, word2

def encrypt_decrypt():
    test_word = word_entry.get()
    length = int(length_entry.get())
    zenit, polar = generate_two_unique_words(length)
    encrypted_word = encrypt(test_word, zenit, polar)
    decrypted_word = decrypt(encrypted_word, zenit, polar)
    messagebox.showinfo("Results", f"Encrypted word: {encrypted_word}\nDecrypted word: {decrypted_word}\nZenit: {zenit}\nPolar: {polar}")

def close_window(event):
    root.destroy()

root = tk.Tk()
root.configure(background='black')
root.bind('<Control-w>', close_window)

word_label = tk.Label(root, text="Word to encrypt:", background='black', foreground='green2')
word_label.pack()

word_entry = tk.Entry(root)
word_entry.pack()

length_label = tk.Label(root, text="Length of unique words:", background='black', foreground='green2')
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

button = tk.Button(root, text="Encrypt and Decrypt", command=encrypt_decrypt, background='black', foreground='green2')
button.pack()

root.mainloop()