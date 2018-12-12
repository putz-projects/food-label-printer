import serial
import printer
import requests
import datetime
import users
import time

from config import BAUD, SERIAL_PORT, DELAY

def print_init():
    """Print a message to indicate that the machine has restarted.
    """

    r = requests.get("https://api.ipify.org")
    ip = r.text
    printer.print_message("I'm Alive!" + "\n" + ip)

def main_loop():
    ser = serial.Serial(SERIAL_PORT, BAUD)

    while True:
        msg = ser.readline().decode().strip()
        lolcode = users.get_lolcode(msg)
        kerb = users.get_kerb(lolcode)

        if kerb:
            printer.print_label(kerb, datetime.datetime.now())
        else:
            printer.print_message("LOLcode: " + lolcode)

        time.sleep(DELAY)

if __name__ == '__main__':
    print('Starting label printer software!')
    print_init()
    main_loop()
