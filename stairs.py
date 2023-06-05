import pymel.core as pm
import maya.cmds as cmds
from random import randint, choice

cmds.select(all=True)
cmds.delete()

whiteBlinn = cmds.shadingNode("blinn", asShader=True)
cmds.setAttr(whiteBlinn + '.color', 1, 1, 1)

cube_size = 1

nbr = 0;

for x in range(4):
    cube = pm.polyCube(
           name='cube_{}_{}'.format(1, x),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cubeBaseColorBlinn = cmds.shadingNode("blinn", asShader=True)
    cmds.setAttr(cubeBaseColorBlinn + '.color', 1, 1, 1) # White
    cmds.select('cube_{}_{}'.format(1, x))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set(0, nbr*0.25, x*cube_size)
    nbr = nbr + 1

for y in range(4):
    cube = pm.polyCube(
           name='cube_{}_{}'.format(2, y),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cmds.select('cube_{}_{}'.format(2, y))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set(-(y+1)*(cube_size), nbr*0.25, 3)
    nbr = nbr + 1

for v in range(2):
    cube = pm.polyCube(
           name='cube_{}_{}'.format(3, v),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cmds.select('cube_{}_{}'.format(3, v))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set(-4, nbr*0.25, -(v-2)*cube_size)
    nbr = nbr + 1

for w in range(2):
    cube = pm.polyCube(
           name='cube_{}_{}'.format(4, w),
           width=cube_size, height=cube_size, depth=cube_size,
           sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)[0]
    #cmds.polyBevel('cube_{}_{}'.format(1, x), com=0, fraction=0.15, offsetAsFraction=1, autoFit=1, segments=5, 
    #       worldSpace=1, uvAssignment=0, smoothingAngle=30, fillNgons=1, mergeVertices=1,
    #       mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)
    cmds.select('cube_{}_{}'.format(4, w))
    cmds.hyperShade(assign=cubeBaseColorBlinn)
    cube.translate.set((w-3)*(cube_size), nbr*0.25, 1)
    nbr = nbr + 1


