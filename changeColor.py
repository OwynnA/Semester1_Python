import maya.cmds as cmds

def changeColor(color):
    sels = cmds.ls (sl = True)
    if len(sels) == 0:
        cmds.error("select object before running ChangeColor().")

    if color < 0 or color > 31:
        color = 0
        cmds.warning("color argument must be within 0 and 31. Value set to default of 0")

    for i in range(len(sels)):
        shapes = cmds.listRelatives(sels[i], s = True)
        for shape in shapes:
            cmds.setAttr(shape + '.overrideEnabled', 1)
            cmds.setAttr(shape + '.overrideColor', color)

changeColor(6)
