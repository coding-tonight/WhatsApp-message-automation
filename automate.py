from pathlib import Path
import pywhatkit as kit

BASE_DIR = Path(__file__).parent

try:
    with open(BASE_DIR / 'phone.txt' ,'r') as file:
        phone_numbers = [phone_number.strip() for phone_number in file]

except FileNotFoundError as exe:
    raise FileNotFoundError('phone.txt does not exits') from exe
        

message = input('Enter message you want to send:\n')

def sendMessage(phone_numbers, message):
    try:
        for phone_number in phone_numbers:
            kit.sendwhatmsg_instantly(phone_number, message, wait_time=8, tab_close=True)
    
    except ConnectionAbortedError as exe:
        raise Exception(exe)
    

sendMessage(phone_numbers, message)



