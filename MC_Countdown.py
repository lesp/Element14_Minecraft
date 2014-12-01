import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()
n = 5
while n > 0:
    mc.postToChat(str(n))
    sleep(1)
    n = n - 1
