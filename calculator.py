import maya.cmds as cmds

otherOperations = 5

def add(input_list):
    return sum(input_list)

def power(input_list, exponent):
    return input_list ** exponent

def mean(input_list):
    return sum(input_list) / len(input_list)

def median(input_list):
    sorted_input  = sorted(input_list)
    even = len(input_list) % 2
    if even == 1:
        spot = len(input_list) // 2
        return sorted_input[spot]
    else:
        spot = len(input_list) // 2
        spot2 = spot - 1
        return (sorted_input[spot] + sorted_input[spot2]) /2

def shown_text(value):
    print(value)
    global otherOperations
    text_field = cmds.optionVar(query = "ftNameField")
    text = cmds.textField(text_field, text = True, query =True)
    cmds.textField(text_field, edit=True, text=(text + value))

def function_switch(input_val):
    global otherOperations
    if input_val == 0:
        otherOperations = 0
        shown_text("^")
    elif input_val ==1:
        otherOperations = 1
        shown_text(" ")
    elif input_val == 2:
        otherOperations = 2
        shown_text(" ")

def evaluate():
    global otherOperations
    text_field = cmds.textField("ftNameField", query=True, text=True)
    if otherOperations == 0:
        array = text_field.split("^")
        base = float(array[0])
        expo = int(array[1])
        result = str(power(base, expo))
        cmds.textField("ftNameField", edit=True, text=result)
        otherOperations = 5

    elif otherOperations == 1:
        array = text_field.split(" ")
        array2 = [float(i) for i in array]
        result = str(mean(array2))
        cmds.textField("ftNameField", edit=True, text=result)
        otherOperations = 5

    elif otherOperations == 2:
        array = text_field.split(" ")
        array2 = [float(i) for i in array]
        result = str(median(array2))
        cmds.textField("ftNameField", edit=True, text=result)
        otherOperations = 5

    else:
        result = eval(text_field)
        cmds.textField("ftNameField", edit=True, text=result)

def clear():
    global otherOperations
    cmds.textField("ftNameField", edit=True, text="")
    otherOperations = 5

def calculator_ui():
    mWindow = "CalculatorWindow"
    if cmds.window(mWindow, exists = True):
        cmds.deleteUI(mWindow)

    cmds.window(mWindow, title = "Calculator", widthHeight =(310, 400))
    mColumn = cmds.columnLayout(adjustableColumn = True)

    cmds.optionVar(sv = ("ftNameField", cmds.textField('ftNameField', editable = False)))


    row1 = cmds.rowLayout(numberOfColumns = 4, adjustableColumn = 4, parent = mColumn)
    column1 = cmds.columnLayout(p = row1, adjustableColumn = True, width = 75)
    cmds.button(label = "exponent", command = lambda x: function_switch(0))
    cmds.button(label = "1", command=lambda x: shown_text("1"), p = column1)
    cmds.button(label = "4", command=lambda x: shown_text("4"), p = column1)
    cmds.button(label = "7", command=lambda x: shown_text("7"), p = column1)
    cmds.button(label = ".", command=lambda x: shown_text("."), p = column1)
    column2 = cmds.columnLayout(p = row1, adjustableColumn = True, width = 75)
    cmds.button(label="mean", command=lambda x: function_switch(1))
    cmds.button(label="2", command=lambda x: shown_text("2"), p=column2)
    cmds.button(label="5", command=lambda x: shown_text("5"), p=column2)
    cmds.button(label="8", command=lambda x: shown_text("8"), p=column2)
    cmds.button(label="0", command=lambda x: shown_text("0"), p=column2)
    column3 = cmds.columnLayout(p=row1, adjustableColumn=True, width=75)
    cmds.button(label="median", command=lambda x: function_switch(2))
    cmds.button(label="3", command=lambda x: shown_text("3"), p=column3)
    cmds.button(label="6", command=lambda x: shown_text("6"), p=column3)
    cmds.button(label="9", command=lambda x: shown_text("9"), p=column3)
    cmds.button(label="=", command=lambda x: evaluate(), p=column3)
    column4 = cmds.columnLayout(p=row1, adjustableColumn=True, width=75)
    cmds.button(label="clear", command=lambda x: clear())
    cmds.button(label="+", command=lambda x: shown_text("+"), p=column4)
    cmds.button(label="-", command=lambda x: shown_text("-"), p=column4)
    cmds.button(label="*", command=lambda x: shown_text("*"), p=column4)
    cmds.button(label="/", command=lambda x: shown_text("/"), p=column4)

    cmds.showWindow(mWindow)

calculator_ui()