import hou

def mergeCopiedNodes():
    network = hou.ui.curDesktop().paneTabUnderCursor()
    networkPath = network.pwd().path()
    pos = network.cursorPosition()

    copiedNodes = hou.ui.getTextFromClipboard()

    newPos = 0

    if copiedNodes:
        list = copiedNodes.split()
        for item in list:
            if hou.node(item) != None:
                merge = hou.node(networkPath).createNode('object_merge','IN_'+item.split('/')[-1])
                merge.parm('objpath1').set(str(item))
                merge.parm('xformtype').set(1)
                merge.setPosition(pos)
                merge.move([newPos*2,0])
                if newPos == 0:
                    merge.setSelected(True,True)
                else:
                    merge.setSelected(True,False)
                newPos = newPos + 1


mergeCopiedNodes()
