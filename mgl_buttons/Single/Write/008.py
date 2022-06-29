#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Render current frame
#
#----------------------------------------------------------------------------------------------------------

nuke.execute(nuke.selectedNode(), nuke.frame(), nuke.frame())
print('Render : ', nuke.frame())