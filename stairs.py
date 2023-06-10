import pymel.core as pm
import maya.cmds as cmds
from random import randint, choice

def createPenrose():
    
    #CLEAR EVERYTHING
    cmds.select(all=True)
    cmds.delete()
    
    #CREATE STAIRS
    whiteBlinn = cmds.shadingNode("blinn", asShader=True)
    cmds.setAttr(whiteBlinn + '.color', 1, 1, 1)

    cube_size = 1
    index = 0

    for x in range(4):
        cube = pm.polyCube(
               name='cube_{}'.format(index),
               width=cube_size, height=cube_size, depth=cube_size,
               sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
        cubeBaseColorBlinn = cmds.shadingNode("blinn", asShader=True)
        cmds.setAttr(cubeBaseColorBlinn + '.color', 0, 0.05, 0.1) # White
        cmds.select('cube_{}'.format(index))
        cmds.hyperShade(assign=cubeBaseColorBlinn)
        cube.translate.set(0, index*0.25, x*cube_size)
        index = index + 1

    for y in range(4):
        cube = pm.polyCube(
               name='cube_{}'.format(index),
               width=cube_size, height=cube_size, depth=cube_size,
               sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
        cmds.select('cube_{}'.format(index))
        cmds.hyperShade(assign=cubeBaseColorBlinn)
        cube.translate.set(-(y+1)*(cube_size), index*0.25, 3)
        index = index + 1

    for v in range(2):
        cube = pm.polyCube(
               name='cube_{}'.format(index),
               width=cube_size, height=cube_size, depth=cube_size,
               sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
        cmds.select('cube_{}'.format(index))
        cmds.hyperShade(assign=cubeBaseColorBlinn)
        cube.translate.set(-4, index*0.25, -(v-2)*cube_size)
        index = index + 1

    for w in range(2):
        cube = pm.polyCube(
               name='cube_{}'.format(index),
               width=cube_size, height=cube_size, depth=cube_size,
               sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
        cmds.select('cube_{}'.format(index))
        cmds.hyperShade(assign=cubeBaseColorBlinn)
        cube.translate.set((w-3)*(cube_size), index*0.25, 1)
        index = index + 1

    #TRICK FOR PENROSE

    cmds.select('cube_11.f[0]')
    cmds.delete()
    cmds.select('cube_11.f[2]')
    cmds.delete()
    cmds.select('cube_11.f[2]')
    cmds.delete()

    cmds.select('cube_11.e[0]')
    cmds.polySubdivideEdge(ws=0, s=0, dv=1, ch=1)

    cmds.select('cube_11.vtx[7]')
    cmds.move(-2.248, 3.115, 1.377)
    cmds.select('cube_11.vtx[2]')
    cmds.move(-1.508, 3.270, 1.429)

    #SET CAMERA POSITION

    cmds.select('persp')
    cmds.move(-13.021, 16.090, 7.415)
    cmds.rotate(-49.818, -63.921, -0.898)

def revealTrick():
    
    #CAMERA POSITION
    
    cmds.select('persp')
    cmds.move(-13.021, 16.090, 7.415)
    cmds.rotate(-49.818, -63.921, -0.898)
    
    cameraT0x = -13.021
    cameraT0y = 16.090
    cameraT0z = 7.415
    cameraR0x = -49.818
    cameraR0y = -63.921
    cameraR0z = -0.898

    cameraTx = -10.518
    cameraTy = 2.690
    cameraTz = -15.843
    cameraRx = -5.203
    cameraRy = -153.944
    cameraRz = 0.439

    DcameraTx = cameraTx - cameraT0x
    DcameraTy = cameraTy - cameraT0y
    DcameraTz = cameraTz - cameraT0z
    DcameraRx = cameraRx - cameraR0x
    DcameraRy = cameraRy - cameraR0y
    DcameraRz = cameraRz - cameraR0z
    
    #CREATE SPHERE

    cmds.sphere(name = 'ball', r=0.30  )
    cmds.select('ball')
    cmds.move(-2,3.5,1)
    for i in range (0, 4):
        for j in range (0, 8):
            ballBaseColorBlinn = cmds.shadingNode("blinn", asShader=True)
            if ((j % 2) == 1):
                cmds.setAttr(ballBaseColorBlinn + '.color', 0, 0, 1) # White
            else:
                cmds.setAttr(ballBaseColorBlinn + '.color', 0, 1, 0) # White
            cmds.select('ball.sf[{}][{}]'.format(i, j))
            cmds.hyperShade(assign=ballBaseColorBlinn)

    texture_path = "C:/Users/sacha/Documents/test3.PNG"
    cmds.select('ball')
    lambert_material = cmds.shadingNode('lambert', asShader=True)
    file_node = cmds.shadingNode('file', asTexture=True)
    cmds.setAttr(file_node + '.fileTextureName', texture_path, type="string")
    cmds.connectAttr(file_node + '.outColor', lambert_material + '.color')
    cmds.select(ball)
    cmds.hyperShade(assign=lambert_material)

    #MOVE SPHERE

    pos0x = -2
    pos0y = 3.5
    pos0z = 1
    posx = -2
    posy = 3.5
    posz = 1
    tstart = 0
    tframe = 24
    id = index - 1
    h = 0
    rx = 0
    rz = 0

    cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=0 )
    cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=0 )
    cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=0 )
    cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=0 )
    cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=0 )
    cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=0 )

    for z in range(0, 23):
        h = h + 1
        cmds.setKeyframe( 'ball', attribute='translateX', value=pos0x, t=h )
        cmds.setKeyframe( 'ball', attribute='translateY', value=pos0y, t=h )
        cmds.setKeyframe( 'ball', attribute='translateZ', value=pos0z, t=h )
        cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
        cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
        cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )

    for i in range (0, index - 1):
        if (id == 0):
            id = 12
        cube_position = pm.PyNode('cube_{}'.format(id - 1)).getTranslation()
        deltax = cube_position.x - pos0x
        deltay = cube_position.y - pos0y + 0.75
        deltaz = cube_position.z - pos0z
        frame = 0
        if (deltax < -0.5):
            rotatex = 0
            rotatez = 180
        if (deltax > 0.5):
            rotatex = 0
            rotatez = -180
        if (deltaz > 0.5):
            rotatex = 180
            rotatez = 0
        if (deltaz < -0.5):
            rotatex = -180
            rotatez = 0
        for time in range (0, 14):
            posx = pos0x + deltax * frame / 24
            #posy = pos0y + deltay * frame / 24
            posz = pos0z + deltaz * frame / 24
            rx = rx + rotatex / 24
            rz = rz + rotatez / 24
            h = h + 1
            cmds.setKeyframe( 'ball', attribute='translateX', value=posx, t=h )
            cmds.setKeyframe( 'ball', attribute='translateY', value=posy, t=h )
            cmds.setKeyframe( 'ball', attribute='translateZ', value=posz, t=h )
            cmds.setKeyframe( 'ball', attribute='rotateX', value=rx, t=h )
            cmds.setKeyframe( 'ball', attribute='rotateZ', value=rz, t=h )
            if (h <= 200):
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )
            elif (h > 200 and h < 260):
                print(h)
                cameraT0x = cameraT0x + DcameraTx / 60
                cameraT0y = cameraT0y + DcameraTy / 60
                cameraT0z = cameraT0z + DcameraTz / 60
                cameraR0x = cameraR0x + DcameraRx / 60
                cameraR0y = cameraR0y + DcameraRy / 60
                cameraR0z = cameraR0z + DcameraRz / 60
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )
            else:
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraTx, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraTy, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraTz, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraRx, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraRy, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraRz, t=h )
            frame = frame + 1
        for time in range (0, 4):
            posx = pos0x + deltax * frame / 24
            posy = pos0y + deltay * time / 4
            posz = pos0z + deltaz * frame / 24
            rx = rx + rotatex / 24
            rz = rz + rotatez / 24
            h = h + 1
            cmds.setKeyframe( 'ball', attribute='translateX', value=posx, t=h )
            cmds.setKeyframe( 'ball', attribute='translateY', value=posy, t=h )
            cmds.setKeyframe( 'ball', attribute='translateZ', value=posz, t=h )
            cmds.setKeyframe( 'ball', attribute='rotateX', value=rx, t=h )
            cmds.setKeyframe( 'ball', attribute='rotateZ', value=rz, t=h )
            if (h <= 200):
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )
            elif (h > 200 and h < 260):
                print(h)
                cameraT0x = cameraT0x + DcameraTx / 60
                cameraT0y = cameraT0y + DcameraTy / 60
                cameraT0z = cameraT0z + DcameraTz / 60
                cameraR0x = cameraR0x + DcameraRx / 60
                cameraR0y = cameraR0y + DcameraRy / 60
                cameraR0z = cameraR0z + DcameraRz / 60
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )
            else:
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraTx, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraTy, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraTz, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraRx, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraRy, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraRz, t=h )
            frame = frame + 1
        for time in range (0, 6):
            posx = pos0x + deltax * frame / 24
            #posy = pos0y + deltay * frame / 24
            posz = pos0z + deltaz * frame / 24
            rx = rx + rotatex / 24
            rz = rz + rotatez / 24
            h = h + 1
            cmds.setKeyframe( 'ball', attribute='translateX', value=posx, t=h )
            cmds.setKeyframe( 'ball', attribute='translateY', value=posy, t=h )
            cmds.setKeyframe( 'ball', attribute='translateZ', value=posz, t=h )
            cmds.setKeyframe( 'ball', attribute='rotateX', value=rx, t=h )
            cmds.setKeyframe( 'ball', attribute='rotateZ', value=rz, t=h )
            if (h <= 200):
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )
            elif (h > 200 and h < 260):
                print(h)
                cameraT0x = cameraT0x + DcameraTx / 60
                cameraT0y = cameraT0y + DcameraTy / 60
                cameraT0z = cameraT0z + DcameraTz / 60
                cameraR0x = cameraR0x + DcameraRx / 60
                cameraR0y = cameraR0y + DcameraRy / 60
                cameraR0z = cameraR0z + DcameraRz / 60
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraT0x, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraT0y, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraT0z, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraR0x, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraR0y, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraR0z, t=h )
            else:
                cmds.setKeyframe( 'persp', attribute='translateX', value=cameraTx, t=h )
                cmds.setKeyframe( 'persp', attribute='translateY', value=cameraTy, t=h )
                cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraTz, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraRx, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraRy, t=h )
                cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraRz, t=h )
            frame = frame + 1
        tstart = tframe
        tframe = tframe + 24
        pos0x = posx
        pos0y = posy
        pos0z = posz
        id = id - 1

    for time in range (0, 6):
        posx = posx - 3 / 24
        rx = rx + 0 / 24
        rz = rz + 180 / 24
        cmds.setKeyframe( 'ball', attribute='rotateX', value=rx, t=h )
        cmds.setKeyframe( 'ball', attribute='rotateZ', value=rz, t=h )
        cmds.setKeyframe( 'ball', attribute='translateX', value=posx, t=h )
        cmds.setKeyframe( 'persp', attribute='translateX', value=cameraTx, t=h )
        cmds.setKeyframe( 'persp', attribute='translateY', value=cameraTy, t=h )
        cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraTz, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraRx, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraRy, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraRz, t=h )
        h = h + 1

    for time in range (0, 24):
        posy = posy - 3 / 24
        posx = posx - 3 / 100
        rx = rx + 0 / 24
        rz = rz + 180 / 24
        cmds.setKeyframe( 'ball', attribute='rotateX', value=rx, t=h )
        cmds.setKeyframe( 'ball', attribute='rotateZ', value=rz, t=h )
        cmds.setKeyframe( 'ball', attribute='translateY', value=posy, t=h )
        cmds.setKeyframe( 'ball', attribute='translateX', value=posx, t=h )
        cmds.setKeyframe( 'persp', attribute='translateX', value=cameraTx, t=h )
        cmds.setKeyframe( 'persp', attribute='translateY', value=cameraTy, t=h )
        cmds.setKeyframe( 'persp', attribute='translateZ', value=cameraTz, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateX', value=cameraRx, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateY', value=cameraRy, t=h )
        cmds.setKeyframe( 'persp', attribute='rotateZ', value=cameraRz, t=h )
        h = h + 1
    cmds.select( clear=True )
    cmds.currentTime(1, edit=True)
    cmds.play( forward=True )

#INTERFACE

def createInterface():
    myWindow = cmds.window(title="PENROSE", widthHeight=(400, 100))
    cmds.columnLayout(backgroundColor=(0.2, 0.2, 0.2))

    cmds.separator(style='in')
    cmds.separator(style='in')
    cmds.separator(style='in')
    cmds.separator(style='in')
    cmds.separator(style='in')
    cmds.separator(style='in')
    
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 100), (2, 200), (3, 100)])
    cmds.separator(style='none')
    cmds.button(label="Create impossible Penrose stairs", command="createPenrose()", bgc=(0.9, 0.9, 0.7))
    cmds.separator(style='none')
    cmds.separator(style='none');cmds.separator(style='none', height = 5);cmds.separator(style='none')
    cmds.separator(style='none');cmds.separator(style='none');cmds.separator(style='none')

    cmds.separator(style='none')
    cmds.button(label="Reveal trick", command="revealTrick()", bgc=(0, 0, 0.15))
    cmds.separator(style='none')
    cmds.showWindow(myWindow)

createInterface()