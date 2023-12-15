import maya.cmds as cmds
import random

def scatter(duplicate, xMin, xMax, yMin, yMax, zMin, zMax):
    sels = cmds.ls (sl = True)

    for i in range(len(sels)):
        for a in range(duplicate):
            dups = cmds.duplicate(sels[i], rr=True)
            dup = dups[0]

            randX = random.randrange(xMin, xMax)
            randY = random.randrange(yMin, yMax)
            randZ = random.randrange(zMin, zMax)

            cmds.xform(dup, ws = True, t = (randX, randY, randZ))
def ButtonCmd():
    dupField = cmds.optionVar(q="dup")
    xMinField = cmds.optionVar(q="xMin")
    xMaxField = cmds.optionVar(q="xMax")
    yMinField = cmds.optionVar(q="yMin")
    yMaxField = cmds.optionVar(q="yMax")
    zMinField = cmds.optionVar(q="zMin")
    zMaxField = cmds.optionVar(q="zMax")

    dup = int(cmds.intField(dupField, query = True, value = True))
    xMin = float(cmds.floatField(xMinField, query=True, value=True))
    xMax = float(cmds.floatField(xMaxField, query=True, value=True))
    yMin = float(cmds.floatField(yMinField, query=True, value=True))
    yMax = float(cmds.floatField(yMaxField, query=True, value=True))
    zMin = float(cmds.floatField(zMinField, query=True, value=True))
    zMax = float(cmds.floatField(zMaxField, query=True, value=True))

    scatter(dup, xMin, xMax, yMin, yMax, zMin, zMax)
def scatterUI ():
    mWindow = "ScatterWindow"
    if cmds.window(mWindow, exists = True):
        cmds.deleteUI(mWindow)

    cmds.window(mWindow, title = "Scatter", widthHeight = (210, 150))
    mColumn = cmds.columnLayout(adjustableColumn = True)
    cmds.text(label="Number of Duplicates", fn="boldLabelFont", al="left", p=mColumn)
    cmds.optionVar(sv=("dup", cmds.intField('xMin', editable=True)))

    cmds.text(label="X Range", fn="boldLabelFont", al="left", p=mColumn)
    row1 = cmds.rowLayout(numberOfColumns=4, adjustableColumn=4, parent=mColumn)
    column1 = cmds.columnLayout(p=row1, adjustableColumn=True, width=40)
    column2 = cmds.columnLayout(p=row1, adjustableColumn=True, width=60)
    column3 = cmds.columnLayout(p=row1, adjustableColumn=True, width=40)
    column4 = cmds.columnLayout(p=row1, adjustableColumn=True, width=60)
    cmds.text(label="min", fn="boldLabelFont", al="left", p=column1)
    cmds.optionVar(sv=("xMin", cmds.floatField('xMin', editable=True, p=column2)))
    cmds.text(label="max", fn="boldLabelFont", al="left", p=column3)
    cmds.optionVar(sv=("xMax", cmds.floatField('xMax', editable=True, p=column4)))

    cmds.text(label="Y Range", fn="boldLabelFont", al="left", p=mColumn)
    row2 = cmds.rowLayout(numberOfColumns=4, adjustableColumn=4, parent=mColumn)
    column5 = cmds.columnLayout(p=row2, adjustableColumn=True, width=40)
    column6 = cmds.columnLayout(p=row2, adjustableColumn=True, width=60)
    column7 = cmds.columnLayout(p=row2, adjustableColumn=True, width=40)
    column8 = cmds.columnLayout(p=row2, adjustableColumn=True, width=60)
    cmds.text(label="min", fn="boldLabelFont", al="left", p=column5)
    cmds.optionVar(sv=("yMin", cmds.floatField('yMin', editable=True, p=column6)))
    cmds.text(label="max", fn="boldLabelFont", al="left", p=column7)
    cmds.optionVar(sv=("yMax", cmds.floatField('yMax', editable=True, p=column8)))


    cmds.text(label="Z Range", fn="boldLabelFont", al="left", p=mColumn)
    row3 = cmds.rowLayout(numberOfColumns=4, adjustableColumn=4, parent=mColumn)
    column9 = cmds.columnLayout(p=row3, adjustableColumn=True, width=40)
    column10 = cmds.columnLayout(p=row3, adjustableColumn=True, width=60)
    column11 = cmds.columnLayout(p=row3, adjustableColumn=True, width=40)
    column12 = cmds.columnLayout(p=row3, adjustableColumn=True, width=60)
    cmds.text(label="min", fn="boldLabelFont", al="left", p=column9)
    cmds.optionVar(sv=("zMin", cmds.floatField('zMin', editable=True, p=column10)))
    cmds.text(label="max", fn="boldLabelFont", al="left", p=column11)
    cmds.optionVar(sv=("zMax", cmds.floatField('zMax', editable=True, p=column12)))

    cmds.button(label="Everybody Scatter!", command = lambda x: ButtonCmd(), p=mColumn)

    cmds.showWindow(mWindow)
scatterUI()