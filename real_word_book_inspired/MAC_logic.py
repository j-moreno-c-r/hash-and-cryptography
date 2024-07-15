from sub_tools.mix_strs import mix

if __name__ == "__main__":
    def main():      
        import hashlib
        users = {}
        entrace_name = str(input("Enter your User name: "))
        entrace_key =  str(input("Enter your password: "))
        mixed_entrace = mix(entrace_name, entrace_key)
        mac = hashlib.sha256(mixed_entrace.encode()).hexdigest() 
        users[entrace_name] = mac
        print(f"This is your user name and cookie {users}")
        print(':-'*30)
        username = input("now lets try login, entry your user name, and wee will check your saved key: ")
        if username in users:
            if users[username] == mac:
                print(" 🖖 ✅ logged")
        else:
            print("🖕 ❗ Username are not registered, try again...")

    main()

