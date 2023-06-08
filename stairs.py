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
    cmds.setAttr(cubeBaseColorBlinn + '.color', 1, 1, 1) # Black
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

#CREATE SPHERE

cmds.sphere(name = 'ball', r=0.30  )
cmds.select('ball')
cmds.move(-2,3.5,1)

#MOVE SPHERE

pos0x = -2
pos0y = 3.5
pos0z = 1
tstart = 0
tframe = 24
id = index - 1
h = 0

for i in range (0, index):
    if (id == 0):
        id = 12
    cube_position = pm.PyNode('cube_{}'.format(id - 1)).getTranslation()
    deltax = cube_position.x - pos0x
    deltay = cube_position.y - pos0y + 0.75
    deltaz = cube_position.z - pos0z
    print (i)
    for time in range (0, 24):
        posx = pos0x + deltax * time / 24
        posy = pos0y + deltay * time / 24
        posz = pos0z + deltaz * time / 24
        h = h + 1
        cmds.setKeyframe( 'ball', attribute='translateX', value=posx, t=h )
        cmds.setKeyframe( 'ball', attribute='translateY', value=posy, t=h )
        cmds.setKeyframe( 'ball', attribute='translateZ', value=posz, t=h )
    tstart = tframe
    tframe = tframe + 24
    pos0x = posx
    pos0y = posy
    pos0z = posz
    id = id - 1


