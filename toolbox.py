import maya.cmds as cmds
import color


class Toolbox:
    window_name = "why"
    def __init__(self):
        pass
    def delete(self):
        if cmds.window(Toolbox.window_name, exists = True):
            cmds.deleteUI(Toolbox.window_name)
    def create(self):
        #self.delete()
        self.window_name = cmds.window(Toolbox.window_name, title = "Toolbox", widthHeight = (300,400))
        mColumn = cmds.columnLayout(adjustableColumn = True)
        cmds.text(label = "Tools", fn="boldLabelFont", al="left", p=mColumn)
        cmds.button(label = "Color Changer")
        cmds.showWindow(Toolbox.window_name)
        print("AAAAAAAAAA")


test = Toolbox()
test.create()