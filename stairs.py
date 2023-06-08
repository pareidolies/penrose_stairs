import pymel.core as pm
import maya.cmds as cmds
from random import randint, choice

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
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cubeBaseColorBlinn = cmds.shadingNode("blinn", asShader=True)
    cmds.setAttr(cubeBaseColorBlinn + '.color', 1, 1, 1) # White
    cmds.select('cube_{}'.format(index))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set(0, index*0.25, x*cube_size)
    index = index + 1

for y in range(4):
    cube = pm.polyCube(
           name='cube_{}'.format(index),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cmds.select('cube_{}'.format(index))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set(-(y+1)*(cube_size), index*0.25, 3)
    index = index + 1

for v in range(2):
    cube = pm.polyCube(
           name='cube_{}'.format(index),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cmds.select('cube_{}'.format(index))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set(-4, index*0.25, -(v-2)*cube_size)
    index = index + 1

for w in range(2):
    cube = pm.polyCube(
           name='cube_{}'.format(index),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cmds.select('cube_{}'.format(index))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set((w-3)*(cube_size), index*0.25, 1)
    index = index + 1

#TRICK FOR PENROSE

cmds.delete('cube_11.f[0]')
cmds.delete('cube_11.f[2]')
cmds.delete('cube_11.f[3]')

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


#CREATE SPHERE

cmds.sphere(name = 'ball', r=0.30  )
cmds.select('ball')
cmds.move(-2,3.5,1)
for i in range (0, 3):
    for j in range (1, 8):
        ballBaseColorBlinn = cmds.shadingNode("blinn", asShader=True)
        if ((j % 2) == 1):
            cmds.setAttr(ballBaseColorBlinn + '.color', 0, 0, 1) # White
        else:
            cmds.setAttr(ballBaseColorBlinn + '.color', 0, 1, 0) # White
        cmds.select('ball.sf[{}][{}]'.format(i, j))
        cmds.hyperShade(assign=ballBaseColorBlinn)

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

for i in range (0, index - 1):
    if (id == 0):
        id = 12
    cube_position = pm.PyNode('cube_{}'.format(id - 1)).getTranslation()
    deltax = cube_position.x - pos0x
    deltay = cube_position.y - pos0y + 0.75
    deltaz = cube_position.z - pos0z
    print (deltax)
    print (deltay)
    print (deltaz)
    print (i)
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
    for time in range (0, 10):
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
        frame = frame + 1
    for time in range (0, 10):
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
        frame = frame + 1
    tstart = tframe
    tframe = tframe + 24
    pos0x = posx
    pos0y = posy
    pos0z = posz
    id = id - 1

for time in range (0, 24):
    posy = posy - 3 / 24
    cmds.setKeyframe( 'ball', attribute='translateY', value=posy, t=h )
    h = h + 1

