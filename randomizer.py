import maya.cmds as cmds
import random

def scatter(duplicate, xMin, xMax, yMin, yMax, zMin, zMax):
    sels = cmds.ls (sl = True)

    for i in range(len(sels)):
        for a in range(duplicate):
            dups = cmds.duplicate(sels[i], rr=True)
            dup = dups[0]

            randX = random.randint(xMin, xMax)
            randY = random.randint(yMin, yMax)
            randZ = random.randint(zMin, zMax)

            cmds.xform(dup, ws = True, t = (randX, randY, randZ))

scatter(3, 0, 20, 0, 20, 0, 20)