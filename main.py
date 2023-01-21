import secrets
import string

def generate_password():
    f = open("pw.txt", "w")
    length = 0
    while length < 8 or length > 20: #loopas, kad paprasyti pw
        length = int(input("Enter the desired password length (between 8 and 20 characters):\n"))  # papraso slaptazodzio ilgio
        if length < 8 or length > 20: #jeigu jis yra trupesnis negu 8 simboliai arba ilgesnis negu 20 simboliu siuncia errora ir praso is naujo
            print("Error: password length must be between 8 and 20 characters.")
    else:
        alphabet = string.ascii_letters + string.digits #skaiciai ir raides
        password = ''.join(secrets.choice(alphabet) for i in range(length)) #sugeneruoja ir sujungia random sugeneruotus simbolius
        f.write(password)
        print("Your password is in file called pw.txt in folder")
        f.close()

        ask = input("Do you want some tips?: \n")
        if ask == "yes":
            print('Here are some tips, that will help you:')
            print("If you aren't sure enough that your password is secure, use https://www.passwordmonster.com to check if it's secure enough")
            print("Use a password manager to manage your passwords. Here's one I recommend: https://bitwarden.com ")
        elif ask == "no":
            print("okey")

generate_password()











