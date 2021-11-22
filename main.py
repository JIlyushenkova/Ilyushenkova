from devices.Device import *

from device import read_line, open_device, Device

if __name__ == '__main__':
    try:
        device: Device = open_device('/devices/dev3')


        for i in range(3):
            print(read_line(device))


    except Exception as exception:
        print(f'Error: {exception}')