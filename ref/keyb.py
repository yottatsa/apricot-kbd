
import sys
import time
import serial

import getch

from scans import scans

if len(sys.argv) == 2:
	s = serial.Serial(sys.argv[1], timeout=0.001)
else:
	s = serial.Serial("/dev/tty.usbmodem142101", timeout=0.001)

def sendtime():
	tm_year = 23
	tm_mon = 4
	tm_mday = 8
	tm_wday = 6
	tm_hour = 19
	tm_min = 30
	tm_sec = 0
	pkt = [0] * 13
	pkt[ 0] = 0xF0 | (((tm_year % 100) / 10))
	pkt[ 1] = 0xF0 | ((tm_year % 10))
	pkt[ 2] = 0xF0 | ((tm_mon / 10))
	pkt[ 3] = 0xF0 | ((tm_mon % 10))
	pkt[ 4] = 0xF0 | ((tm_mday / 10))
	pkt[ 5] = 0xF0 | ((tm_mday % 10))
	pkt[ 6] = 0xF0 | ((tm_wday % 10))
	pkt[ 7] = 0xF0 | ((tm_hour / 10))
	pkt[ 8] = 0xF0 | ((tm_hour % 10))
	pkt[ 9] = 0xF0 | ((tm_min / 10))
	pkt[10] = 0xF0 | ((tm_min % 10))
	pkt[11] = 0xF0 | ((tm_sec / 10))
	pkt[12] = 0xF0 | ((tm_sec % 10))
	s.write(pkt)

def procin(sym):
	"""   
    - 01-7f: Character codes for MicroScreen
    - 80-cf: Cursor address
    - f0-f9: BCD data
    """
	sym = ord(sym)
	keys = {
		0xd0: "Clear screen",
		0xd1: "Cursor left",
		0xd2: "Cursor right",
		0xd3: "Cursor on",
		0xd4: "Cursor off",
		0xd5: "Display on",
		0xd6: "Display off",
		0xe0: "Query",
		0xe1: "Time and date request",
		0xe2: "Display time/data on MicroScreen",
		0xe3: "Set LED prefix",
		0xe4: "Set time and date",
		0xe5: "Mouse enable",
		0xe6: "Mouse disable",
		0xe7: "Execute processor diagnostics",
		0xe8: "Keyboard reset",
		0xfa: "Invalid clock data"}

	if sym >= 1 and sym <= 0x7f:
		print("Character %x" % sym)
	elif sym >= 0x80 and sym <= 0xcf:
		print("Cursor movement")
	elif sym >= 0xf0 and sym <= 0xf9:
		print("BCD %d" % (sym - 0xf0))
	elif sym == 0xe8:
		print(keys[0xe8])
		s.write([0xfb])
		time.sleep(0.01)
	elif sym == 0xe1:
		print("Time asked")
		print(keys[0xe1])
		s.write([0xed])
		sendtime()
	elif sym == 0xe3:
		print("LED %s" % s.read(1)) 
	elif sym in keys.keys():
		print(keys[sym])
	else:
		print("Received: %x" % sym)


def procout(sym):
	if sym in scans.keys():
		sending = scans[sym] + list((x+0x80 for x in scans[sym][::-1]))
		s.write(sending)

import threading

class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(getch.getche())

#start the Keyboard thread
kthread = KeyboardThread(procout)




while True:
	symin = s.read(1)
	if symin != b'':
		procin(symin)
