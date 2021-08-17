from xpt2046 import Touch
from gpiozero import Button, DigitalOutputDevice
import board
import busio
from time import sleep

# touch callback
def touchscreen_press(x, y):
    print(x,y)

cs = DigitalOutputDevice(17,active_high=False,initial_value=None)
clk = board.SCLK_1		# same as writing 21
mosi = board.MOSI_1	# same as writing 20
miso = board.MISO_1	# same as writing 19
irq = Button(26)

spi = busio.SPI(clk, mosi, miso)	# auxiliary SPI

xpt = Touch(spi, cs=cs, int_pin=irq, int_handler=touchscreen_press)

while True:
    #print(xpt.get_touch()) # to get the (x, y) coords when you desire
    sleep(.01)
