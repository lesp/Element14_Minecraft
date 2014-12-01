import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    sleep(1)
    mc.postToChat("Your X is "+str(pos.x))
    sleep(1)
    mc.postToChat("Your Y is "+str(pos.y))
    sleep(1)
    mc.postToChat("Your Z is "+str(pos.z))
    
