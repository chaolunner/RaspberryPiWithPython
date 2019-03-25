import serial.tools.list_ports
import datetime
import time

comports = list(serial.tools.list_ports.comports())

if len(comports) <= 0:
    print("No port found!")
else:
    for list_port_info in comports:
        print(list_port_info.device)
        if list_port_info.device == "/dev/rfcomm0":
            serial_port = serial.Serial(list_port_info.device, 9600, timeout=3)
            if serial_port.isOpen() is False:
                serial_port.open()
            serial_port.write(b"connect success!\n")
            while True:
                print(serial_port.readline())
                nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                serial_port.write((str(nowTime) + '\n').encode("UTF-8"))
                time.sleep(1)
