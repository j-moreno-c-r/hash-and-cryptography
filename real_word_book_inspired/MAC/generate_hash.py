def main():      
    import hashlib
    users = []  
    entrace_name = str(input("Enter your User name: "))
    entrace_key =  str(input("Enter your password: "))
    concatened_entrace = entrace_name + entrace_key
    mac = hashlib.sha256(concatened_entrace.encode()).hexdigest() 
    users.append(entrace_name)
    users.append(mac)
    print(f"This is your user name and cookie {users}")
    print(':-'*30)
    cookie = input("now lets try login with you cookie, paste here:")
    if cookie in users:
        print(" 😃 🆗   logged")
    else:
        print("😭 🤨 Or you fucked up or you are a atacker, try again...")

main()

