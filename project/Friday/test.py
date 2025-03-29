import string
import random

LETTEERS = string.ascii_letters
NUMBWES = string.digits
PUNCTUATION = string.punctuation

def password_generator(length=8):
    printable = f'{LETTEERS}{NUMBWES}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k= length)
    password = ''.join(random_password)
    return password
    
def get_password():
    password_length = input("Nhap do dai")
    return int(password_length)

    
def main():
    password_length = get_password()
    password = password_generator(password_length)
    print(password)
    
if __name__ == '__main__':
    main()
