import maya.cmds as cmds

#main house
cmds.polyCube( w = 4, h = 5, d = 8, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-2, 2.5, 0, r = True, os = True, wd = True)

cmds.polyCube( w = 6, h = 4, d = 6, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(3, 2, -1, r = True, os = True, wd = True)

cmds.polyCylinder(r = 2.3, h = 8, sx = 3, sy = 1, sz = 1, ax = [0, 1, 0], rcp = 0, cuv = 3, ch = 1)
cmds.scale(0.48924, 1, 1, r = True)
cmds.rotate(90, 0, 0, r = True, os = True, fo = True)
cmds.rotate(0, 90, 0, r = True, os = True, fo = True)
cmds.move(-2, 5.556, 0, r = True)

cmds.polyCylinder(r = 2.3, h = 5, sx = 3, sy = 1, sz = 1, ax = [0, 1, 0], rcp = 0, cuv = 3, ch = 1)
cmds.scale(0.737, 1.507, 1.507, r = True)
cmds.rotate(0, 0, 90, r = True, os = True, fo = True)
cmds.move(2.233, 4.846, -0.997, r = True)

#roof
cmds.polyCube( w = 3.8, h = .35, d = 8.4, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-0.788, 5.575, 0, r = True, os = True, wd = True)
cmds.rotate(0, 0, -45, r = True, os = True, fo = True)

cmds.polyCube( w = 3.8, h = .35, d = 8.4, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-3.236, 5.575, 0, r = True, os = True, wd = True)
cmds.rotate(0, 0, 45, r = True, os = True, fo = True)

cmds.polyCube( w = 4.792, h = .35, d = 8.22, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(2.094, 5.186, 0.597, r = True, os = True, wd = True)
cmds.rotate(90, 45, 90, r = True, os = True, fo = True)

cmds.polyCube( w = 4.792, h = .35, d = 8.22, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(2.094, 5.186, -2.545, r = True, os = True, wd = True)
cmds.rotate(90, -45, 90, r = True, os = True, fo = True)

#patio
cmds.polyCube( w = 2.204, h = .35, d = 8.22, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(2.108, 3.527, 2.889, r = True, os = True, wd = True)
cmds.rotate(0, 90, 0, r = True, os = True, fo = True)

cmds.polyCube( w = 0.35, h = 3.5, d = .35, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(5.58, 1.75, 3.612, r = True, os = True, wd = True)

cmds.polyCube( w = 0.35, h = 3.5, d = .35, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(0.75, 1.75, 3.612, r = True, os = True, wd = True)

#door
cmds.polyCube( w = 1.413, h = 2.6, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(2.061, 1.3, 2, r = True, os = True, wd = True)

cmds.polyCube( w = 0.35, h = 2.7, d = .35, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(1.229, 1.35, 2.055, r = True, os = True, wd = True)

cmds.polyCube( w = 0.35, h = 2.7, d = .35, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(2.884, 1.35, 2.055, r = True, os = True, wd = True)

cmds.polyCube( w = 2.005, h = .35, d = .35, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(2.056, 2.752, 2.057, r = True, os = True, wd = True)

cmds.polyCylinder(r = 0.047, h = 0.094, sx = 20, sy = 1, sz = 1, ax = [0, 1, 0], rcp = 0, cuv = 3, ch = 1)
cmds.move(1.622, 1.216, 2.133, r = True)
cmds.rotate(90, 0, 0, r = True, os = True, fo = True)

cmds.polySphere(r = 1, sx = 20, sy = 20, ax = [0, 1, 0], cuv = 2, ch = 1)
cmds.scale(0.083, 0.121, 0.082, r = True)
cmds.move(1.62, 1.212, 2.237, r = True)

#window next to the door
cmds.polyCube( w = 0.138, h = 1.361, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(3.748, 1.894, 2.028, r = True, os = True, wd = True)

cmds.polyCube( w = 0.138, h = 1.361, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(5.142, 1.894, 2.028, r = True, os = True, wd = True)

cmds.polyCube( w = 1.546, h = 0.138, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(4.445, 2.593, 2.028, r = True, os = True, wd = True)

cmds.polyCube( w = 1.546, h = 0.138, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(4.445, 1.251, 2.028, r = True, os = True, wd = True)

#the other window
cmds.polyCube( w = 0.138, h = 1.361, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-2.743, 2.209, 4.043, r = True, os = True, wd = True)

cmds.polyCube( w = 0.138, h = 1.361, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-1.34, 2.209, 4.043, r = True, os = True, wd = True)

cmds.polyCube( w = 1.546, h = 0.138, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-2.037, 2.908, 4.043, r = True, os = True, wd = True)

cmds.polyCube( w = 1.546, h = 0.138, d = 0.179, sx = 1, sy = 1, sz = 1, ax = [0, 1, 0], cuv = 4, ch = 1)
cmds.move(-2.037, 1.566, 4.043, r = True, os = True, wd = True)
