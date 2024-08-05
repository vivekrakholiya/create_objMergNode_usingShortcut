import hou , re

def mergeCopiedNodes():
    network = hou.ui.curDesktop().paneTabUnderCursor()
    networkPath = network.pwd().path()
    pos = network.cursorPosition()

    copiedNodes = hou.ui.getTextFromClipboard()

    newPos = 0
    a = 0

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

                # create parameter in refr node
                node = hou.node(item)
                parm_template_group = node.parmTemplateGroup()
            
                for parm in node.parms():
                    if 'op_path' in str(parm.name()):
                        a = str(parm.name()).replace('op_path','')
                    parm_label = "obj_mrg_path_" + str(int(a)+1)
                    par_name = 'op_path' + str(int(a)+1)
                op_path_parm = hou.StringParmTemplate(par_name,parm_label , 1, string_type=hou.stringParmType.NodeReference)
                parm_template_group.addParmTemplate(op_path_parm)
                node.setParmTemplateGroup(parm_template_group)
                node.parm(par_name).set(merge.path())
                        



mergeCopiedNodes()
