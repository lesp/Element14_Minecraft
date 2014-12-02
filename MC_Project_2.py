import mcpi.minecraft as minecraft
import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

mc = minecraft.Minecraft.create()
while True:
    if GPIO.input(17) == False:
        a = (randint(0,100))
        b = (randint(0,100))
        c = (randint(0,100))
        GPIO.wait_for_edge(17, GPIO.FALLING)
        pos = mc.player.getPos()
        mc.player.setPos(a,b,c)
        mc.postToChat("ENERGIZE!!!")
        sleep(5)
