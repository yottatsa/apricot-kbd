# apricot-kbd
PS/2 to Apricot Xi keyboard translator

## For Arduino Uno

Simple to assemble version that could fit on a prototype board and could be hand-wired.

![Render of a shield PCB on top of Arduino Uno.](https://github.com/yottatsa/apricot-kbd/raw/main/apricot-kbd-uno.jpg)

Firmware: [`apricot-kbd-uno.ino`](https://github.com/yottatsa/apricot-kbd/blob/main/apricot-kbd-uno.ino)

Schematics and PCB: [`schematics-assembly.pdf`](https://github.com/yottatsa/apricot-kbd/blob/main/schematics-assembly.pdf)

BOM:

* 18x24 2.54mm prototype board
* two 1x8 2.54mm pin headers
* [TSR_1-2450](http://www.tracopower.com/products/tsr1.pdf)
* [MC1488](https://www.ti.com/lit/ds/symlink/mc1488.pdf)
* [MC1489](https://www.ti.com/lit/ds/symlink/mc1489.pdf)
* PS/2 Y pigtail or any other way to connect a PS/2 keyboard
* DB9 serial cable pigtail or any other way to connect to Apricot keyboard port
* optional: two DIP-14 sockets


## Standalone ATmega328P

tbd
