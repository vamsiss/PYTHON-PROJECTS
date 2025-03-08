from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_password = fer.decrypt(passw.encode()).decode()
            print("User:", user, ", Password:", decrypted_password)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # Correct encryption process
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
