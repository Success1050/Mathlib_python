from cryptography.fernet import Fernet

def write_key():
    key= Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd= input("what is the master password? ").strip().lower()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for lines in f.readlines():
            data= lines.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {fer.decrypt(passw.encode())}")

def add():
    name= input("Account Name: ")
    pwd= input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n")

while True:
    mode= input("do you want to add or view existing passwords. (view/add)? press q to quit").strip().lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid option")
        continue