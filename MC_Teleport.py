import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
mc.player.setPos(pos.x, pos.y + 50, pos.z + 50)
mc.postToChat("Hello World")
