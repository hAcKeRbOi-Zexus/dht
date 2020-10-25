import time

import Adafruit_DHT

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))


draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

while True:
    para, ho = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((x, top), "Temp={0:0.1f}C  Hum={1:0.1f}%".format(ho, para), font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
