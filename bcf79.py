import os
import json
import requests
from colorama import Fore, Style

def banner():
    os.system("clear")
    print(Fore.GREEN + """
██████╗  ██████╗███████╗███████╗
██╔══██╗██╔════╝██╔════╝██╔════╝
██████╔╝██║     █████╗  █████╗
██╔══██╗██║     ██╔══╝  ██╔══╝
██████╔╝╚██████╗██║     ██║
╚═════╝  ╚═════╝╚═╝     ╚═╝

Bangladesh Cyber Force 79
Owner: Imran
============================
""" + Style.RESET_ALL)

def phone_lookup():
    number = input("Enter Phone Number: ")
    os.system(f"truecallerjs -s {number} --json > result.json")

    try:
        with open("result.json") as f:
            data = json.load(f)
        print(Fore.CYAN + "\n[+] Result:\n")
        print(json.dumps(data, indent=4))
    except:
        print(Fore.RED + "Error fetching data")

def ip_lookup():
    ip = input("Enter IP: ")
    url = f"http://ip-api.com/json/{ip}"
    res = requests.get(url).json()

    print(Fore.YELLOW + "\n[+] IP Info:\n")
    for k, v in res.items():
        print(f"{k} : {v}")

def save_result():
    try:
        with open("result.json") as f:
            data = f.read()
        with open("saved.txt", "a") as s:
            s.write(data + "\n")
        print(Fore.GREEN + "[+] Saved!")
    except:
        print(Fore.RED + "No result found!")

def menu():
    while True:
        banner()
        print("1. Phone Number Lookup")
        print("2. IP Lookup")
        print("3. Save Last Result")
        print("4. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            phone_lookup()
            input("\nPress Enter...")
        elif choice == "2":
            ip_lookup()
            input("\nPress Enter...")
        elif choice == "3":
            save_result()
            input("\nPress Enter...")
        elif choice == "4":
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    menu()
