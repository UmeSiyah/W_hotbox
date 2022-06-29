#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
if any([n.Class() == "BackdropNode" for n in ns]):
    ret = True