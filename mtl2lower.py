import maya.cmds as cmds
import maya.mel as mel

def mtl2lowerLogic():
    for mesh in cmds.ls(type = "mesh"):
        cmds.select(mesh)

        shadingGrps = cmds.listConnections(mesh, type = 'shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps), materials = 1)

        for shader in shaders:
            if shader == shader.lower():
                continue

            if cmds.objExists(shader):
                cmds.rename(shader, shader.lower())

    cmds.confirmDialog(message="Renaming successful!", button=["Ok"], defaultButton="OK", title="Message")

def __createMenu():
    cmds.setParent(mel.eval("$temp1=$gMainWindow"))

    if cmds.control("mtl2lower", exists = True):
        cmds.deleteUI("mtl2lower", menu = True)

    menu = cmds.menu("mtl2lower", label = "mtl2lower", tearOff = True)
    cmds.menuItem(label = "Lowercase Material Names", command = lambda x: mtl2lowerLogic())

__createMenu()
print("mtl2lower initialized!")
