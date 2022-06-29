#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Use as IP
#
#----------------------------------------------------------------------------------------------------------

# author: sbaykal

def createIP():
    nuke.makeGroup()['name'].setValue('Input_Process')
    nuke.toNode('Input_Process')['tile_color'].setValue(1426085375)
    nuke.toNode('Viewer1')['input_process_node'].setValue(nuke.toNode('Input_Process')['name'].getValue())

if nuke.toNode('Input_Process'):
    nuke.delete(nuke.toNode('Input_Process'))
    createIP()
else:
    createIP()
