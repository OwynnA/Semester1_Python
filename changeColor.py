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

def color_change_ui():
    mWindow = "ColorWindow"
    if cmds.window(mWindow, exists = True):
        cmds.deleteUI(mWindow)

    cmds.window(mWindow, title = "Color Change", widthHeight = (500, 300))
    mColumn = cmds.columnLayout(adjustableColumn = True)

    cmds.textField(text = "Neutral Colors", editable = False)
    row1 = cmds.rowLayout(numberOfColumns = 4, adjustableColumn = 4, parent = mColumn)
    column1 = cmds.columnLayout(p = row1, adjustableColumn = True, width = 110)
    column2 = cmds.columnLayout(p=row1, adjustableColumn=True, width=110)
    column3 = cmds.columnLayout(p=row1, adjustableColumn=True, width=110)
    column4 = cmds.columnLayout(p=row1, adjustableColumn=True, width=110)

    cmds.button(label="black", command=lambda x: changeColor(1), p=column1)
    cmds.button(label="default", command=lambda x: changeColor(5), p=column1)
    cmds.button(label="gray", command=lambda x: changeColor(2), p=column2)
    cmds.button(label="selection", command=lambda x: changeColor(19), p=column2)
    cmds.button(label="light gray", command=lambda x: changeColor(3), p=column3)
    cmds.button(label="brown", command=lambda x: changeColor(11), p=column3)
    cmds.button(label="white", command=lambda x: changeColor(16), p=column4)
    cmds.button(label=" ", p=column4)

    cmds.textField(text = "Neon Colors", editable=False, p = mColumn, width = 300)
    row2 = cmds.rowLayout(numberOfColumns=4, adjustableColumn=4, parent=mColumn)
    column5 = cmds.columnLayout(p=row2, adjustableColumn=True, width=110)
    column6 = cmds.columnLayout(p=row2, adjustableColumn=True, width=110)
    column7 = cmds.columnLayout(p=row2, adjustableColumn=True, width=110)
    column8 = cmds.columnLayout(p=row2, adjustableColumn=True, width=110)
    cmds.button(label="red", command=lambda x: changeColor(13), p=column5)
    cmds.button(label="yellow", command=lambda x: changeColor(17), p=column6)
    cmds.button(label="green", command=lambda x: changeColor(14), p=column7)
    cmds.button(label="blue", command=lambda x: changeColor(6), p=column8)

    cmds.textField(text="The Rainbow", editable=False, p=mColumn, width=300)
    row3 = cmds.rowLayout(numberOfColumns=4, adjustableColumn=4, parent=mColumn)
    column9 = cmds.columnLayout(p=row3, adjustableColumn=True, width=110)
    column10 = cmds.columnLayout(p=row3, adjustableColumn=True, width=110)
    column11 = cmds.columnLayout(p=row3, adjustableColumn=True, width=110)
    column12 = cmds.columnLayout(p=row3, adjustableColumn=True, width=110)
    cmds.button(label="red", command=lambda x: changeColor(4), p=column9)
    cmds.button(label="orange", command=lambda x: changeColor(21), p=column9)
    cmds.button(label="dark green", command=lambda x: changeColor(23), p=column9)
    cmds.button(label="baby blue", command=lambda x: changeColor(29), p=column9)
    cmds.button(label="peach", command=lambda x: changeColor(20), p=column9)

    cmds.button(label="orange red", command=lambda x: changeColor(12), p=column10)
    cmds.button(label="yellow", command=lambda x: changeColor(25), p=column10)
    cmds.button(label="forest green", command=lambda x: changeColor(7), p=column10)
    cmds.button(label="sky blue", command=lambda x: changeColor(15), p=column10)
    cmds.button(label="pink", command=lambda x: changeColor(31), p=column10)

    cmds.button(label="burnt orange", command=lambda x: changeColor(10), p=column11)
    cmds.button(label="light green", command=lambda x: changeColor(26), p=column11)
    cmds.button(label="teal", command=lambda x: changeColor(28), p=column11)
    cmds.button(label="purple", command=lambda x: changeColor(30), p=column11)
    cmds.button(label="hot pink", command=lambda x: changeColor(9), p=column11)

    cmds.button(label="light burnt orange", command=lambda x: changeColor(24), p=column12)
    cmds.button(label="green", command=lambda x: changeColor(27), p=column12)
    cmds.button(label="light blue", command=lambda x: changeColor(18), p=column12)
    cmds.button(label="dark purple", command=lambda x: changeColor(8), p=column12)
    cmds.button(label=" ", p=column12)

    cmds.showWindow(mWindow)
color_change_ui()

#neutral: 1, 2, 3, 16, 5, 19, 11
#neon: 13, 17, 14, 6
#rainbow: 4, 12, 10, 24, 21, 25, 26, 27, 23, 7, 28, 18, 29, 15, 30, 8, 20, 31, 9
#1 black 0
#2 gray 0
#3 light gray 0
#4 dark red 0
#5 also default 0
#6 ethereal blue 0
#7 forest green 0
#8 dark purple 0
#9 dark hot pink
#10 burnt orange 0
#11 dark brown 0
#12 orange red 0
#13 neon red 0
#14 neon green 0
#15 medium blue 0
#16 white 0
#17 yellow 0
#18 light blue 0
#19 selection green 0
#20 peach pink
#21 orange 0
#23 light dark green 0
#24 light burnt orange 0
#25 dark yellow 0
#26 dark light green 0
#27 green 0
#28 teal 0
#29 dark light blue 0
#30 purple 0
#31 dark pink