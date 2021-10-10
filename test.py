import requests

option = input("What do you want to do? \n1. Check\n2. Get info\n3. Generate Captcha Key\n\n> ")
if option == "1":
    token = input("Enter Token: ")
    f = requests.get(f"https://discord-api-detectivevoke123.herokuapp.com/check/{token}")
    print(f.text)
elif option == "2":
    token = input("Enter Token: ")
    f = requests.get(f"https://discord-api-detectivevoke123.herokuapp.com/info/{token}")
    print(f.text)
elif option == "3":
    token = input("Enter Token: ")
    f = requests.get(f"https://discord-api-detectivevoke123.herokuapp.com/captcha/")
    print(f.text)
else:
    print("Not an option!")